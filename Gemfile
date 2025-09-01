source 'https://rubygems.org'

# This is the default theme for new Jekyll sites. And this is how you override the theme!
# To publish, set the `remote_theme` in `_config.yml`.
# To remove this, install a theme from RubyGems.org by adding it to the `_config.yml`.
gem "minima", "~> 2.5"

gem "github-pages", group: :jekyll_plugins

# If you want to use GitHub Pages, remove the "gem 'jekyll'" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
# gem "github-pages", group: :jekyll_plugins

# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-remote-theme"
  gem "jekyll-seo-tag"
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :mingw32 do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin, :mingw32]
