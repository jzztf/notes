# jekyll 安装设置

## ruby/gem/bundle

- 国内源: <https://gems.ruby-china.org/>

- 设置

``` bash
# 安装ruby
sudo apt install ruby
# 安装bundler
sudo apt install ruby-bundler

# 替换源
gem sources --add https://gems.ruby-china.org/ --remove https://rubygems.org/
# 查看,确保只有淘宝
gem sources -l

# 使用bundle的config命令
bundle config mirror.https://rubygems.org https://gems.ruby-china.org
# 使用上法,可不单独修改gemfile的source
source 'https://rubygems.org/'
gem 'rails', '4.2.5'
...

# ERROR:  Error installing jekyll:
# ERROR: Failed to build gem native extension.
sudo apt install ruby-dev

```
