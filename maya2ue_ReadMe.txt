=================================================
 maya2ue - Maya to Unreal Engine Exporter
 version: Prototype 0.1.0
-------------------------------------------------
 developed by: TORI(MEOW LABO)
=================================================

◯概要
 - Maya2024向けのスクリプト プラグイン

◯実装されている機能
 - ピボット操作・ベイク処理のアシスト
 - クリーンアップ処理呼出のアシスト
 - UE向けのリネーム&エクスポート処理アシスト

◯使い方
1. Mayaのスクリプトフォルダに "maya2ue" フォルダをそのまま入れてください。
【スクリプトフォルダ例】C:/(ユーザー名)/ドキュメント/maya/(バージョン)/(言語)/scripts

2. Mayaを起動します。既に開いていた場合は、再起動します。

3. スクリプトエディタを開き、Pythonタブを新しく開いてください。

4. 以下の通りに打ち込んで、実行することでウィンドウが開きます。
【初回起動時】import maya2ue
【２回目以降】maya2ue.open()