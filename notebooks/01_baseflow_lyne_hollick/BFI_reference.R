# Baseflow separation using the Lyne and Hollick filter
# Source: Tony Ladson
# https://github.com/TonyLadson/BaseflowSeparation_LyneHollick
# Blog post: https://tonyladson.wordpress.com/2013/10/01/a-standard-approach-to-baseflow-separation-using-the-lyne-and-hollick-filter/
#
# This file is the REFERENCE R implementation.
# The Python translation is in baseflow_lyne_hollick.ipynb

BFI <- function(Q, alpha=0.925, passes=3, ReturnQbase=FALSE, n.reflect=30) {

  FirstPass <- function(Q,a) {
    Qf1 <-  vector('numeric', length=length(Q))
    Qf1[1] <- Q[1]
    for(i in 2:length(Q)) {
      Qf1[i] <- a*Qf1[i-1]+0.5*(1+a)*(Q[i]-Q[i-1])
    }
    Qb1 <- ifelse(Qf1 > 0, Q-Qf1,Q )
    return(data.frame(Qquick = Qf1, Qbase=Qb1))
  }

  BackwardPass <- function(Q,a) {
    Qq <- Q$Qquick
    Qb <- Q$Qbase
    num.rows <- nrow(Q)
    Qf2 <- vector('numeric', length=num.rows)
    Qf2[num.rows] <- Qb[num.rows]
    for(i in (num.rows-1):1) {
      Qf2[i] <- a*Qf2[i+1]+0.5*(1+a)*(Qb[i]-Qb[i+1])
    }
    Qb2 <- ifelse(Qf2 >0, Qb-Qf2,Qb )
    return(data.frame(Qquick = Qf2, Qbase=Qb2))
  }

  ForwardPass <- function(Q,a) {
    Qq <- Q$Qquick
    Qb <- Q$Qbase
    num.rows <- length(Qq)
    Qf2 <- vector('numeric', length=num.rows)
    Qf2[1] <- Qb[1]
    for(i in 2:num.rows) {
      Qf2[i] <- a*Qf2[i-1]+0.5*(1+a)*(Qb[i]-Qb[i-1])
    }
    Qb2 <- ifelse(Qf2 >0, Qb-Qf2,Qb )
    return(data.frame(Qquick = Qf2, Qbase=Qb2))
  }

  BFI.calc <- function(Q, alpha, passes, n.reflect) {
    Qin <- Q
    # Pad with reflected values at start and end to reduce edge effects
    Q.reflect <- vector(mode='numeric', length=length(Q) + 2*n.reflect)
    Q.reflect[1:n.reflect] <- Q[(n.reflect+1):2]
    Q.reflect[(n.reflect+1):(n.reflect + length(Q))] <- Q
    Q.reflect[(n.reflect+length(Q)+1):(length(Q)+2*n.reflect)] <- Q[(length(Q)-1):(length(Q)-n.reflect)]

    Q1 <- FirstPass(Q.reflect,alpha)
    n.pass <- round((passes-1)/2)
    BackwardPass(Q1,alpha)
    for(i in 1:n.pass){
      Q1 <- ForwardPass(BackwardPass(Q1,alpha),alpha)
    }

    Qbase <- Q1$Qbase[(n.reflect+1):(length(Q1$Qbase)-n.reflect)]
    Qbase[Qbase < 0] <- 0
    BFI.value <- sum(Qbase)/sum(Qin)
    return(list(BFI = BFI.value, Qbase = Qbase))
  }

  Flow.index <- function(Q, n.reflect){
    Flow.rle <- rle(is.na(Q))
    if(!any(!Flow.rle$values & Flow.rle$lengths > n.reflect)) stop('Must have at least 31 consecutive non-missing flow values \n')
    index <- which(!Flow.rle$values & Flow.rle$lengths > n.reflect )
    ends <- cumsum(Flow.rle$lengths)[index]
    newindex <- ifelse(index > 1, index-1,0)
    starts <- cumsum(Flow.rle$lengths)[newindex] +1
    if(0 %in% newindex) starts =c(1,starts)
    return(list(starts=starts,ends=ends))
  }

  if(passes %% 2 == 0 | passes < 3) stop('passes must be odd and greater than 2')
  if(alpha < 0 | alpha >=1 ) stop('alpha must be between zero and one \n')
  if(length(Q) <= n.reflect ) stop(paste('n.reflect must be <= length(Q)', ' \n'))

  if(!any(is.na(Q))) {
    BFI.data <- BFI.calc(Q,  alpha, passes, n.reflect)
    BFI.out=BFI.data$BFI
    FractionUsed = 1
    Qbase=BFI.data$Qbase
  }
  else {
    seg.index <- Flow.index(Q, n.reflect)
    seg.num <- length(seg.index$starts)
    w <- numeric(seg.num)
    Q.seg.BFI <- numeric(seg.num)
    Q.seg.Qbase <- rep(NA, times=length(Q))
    for(i in 1:seg.num){
      Q.seg <- Q[seg.index$starts[i]:seg.index$ends[i]]
      w[i] <- length(Q.seg)
      BFI.data <- BFI.calc(Q.seg, alpha, passes, n.reflect)
      Q.seg.BFI[i] <- BFI.data$BFI
      Q.seg.Qbase[seg.index$starts[i]:seg.index$ends[i]] <- BFI.data$Qbase
    }
    BFI.out <- weighted.mean(Q.seg.BFI,w)
    FractionUsed <- sum(w)/sum(!is.na(Q))
    Qbase=Q.seg.Qbase
  }

  if(ReturnQbase){
    return(list(BFI = BFI.out, alpha=alpha, FractionUsed = FractionUsed, Qbase=Qbase))
  } else {
    return(list(BFI = BFI.out, alpha=alpha, FractionUsed = FractionUsed))
  }
}

# ---- Example usage (Bass River at Loch, 67 daily observations) ----
# source('BFI_reference.R')
#
# Q <- c(5,7,108,117,57,36,26,95,1169,308,
#        144,89,62,48,40,35,73,82,342,393,310,
#        275,260,245,256,141,119,934,382,158,96,
#        122,103,83,67,148,366,161,119,82,330,294,
#        261,266,153,247,703,498,286,163,124,85,94,
#        81,62,47,37,30,26,24,24,22,21,20,19,18,18)
#
# BFI(Q, alpha=0.925)
# $BFI      [1] 0.3879...
# $alpha    [1] 0.925
#
# plot(Q, type='l')
# lines(BFI(Q, alpha=0.925, ReturnQbase=TRUE)$Qbase, lty=2, col=4)
