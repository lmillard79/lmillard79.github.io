// Set header background image from data attribute
document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('.page-header[data-overlay-image]');
  if (header) {
    const imageUrl = header.getAttribute('data-overlay-image');
    if (imageUrl) {
      header.style.setProperty('--header-overlay-image', `url('${imageUrl}')`);
    }
  }
});
