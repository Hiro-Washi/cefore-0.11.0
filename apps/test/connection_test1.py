# cefnetdへの接続
import cefpyco

with cefpyco.create_handle() as handle: pass # ブロック開始時にcefnetdへ接続、終了時に切断
