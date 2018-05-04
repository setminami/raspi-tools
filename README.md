# raspi-tools
raspberry pi 3 custom setup tools as TokageCam open submodule

過去のセッションから状態を再現するtoolなので、clean install時のpkg最適化には向かない

## 実験環境反映ツール
### raspi-tools/apt-get-selections.py
`dpkg -l > ../dpkg-l.txt`の内容からパッケージ環境復元
