#######################################################
# Name           : Yayan Multi Brute Facebook (YMBF)  #
# File           : loy.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import time, os

from rich import print as prints
from rich.panel import Panel
from src import cok as tt

O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
M = '\x1b[1;91m' # MERAH

merah  = '[#FF0022]'
hapus  = '[/]'
biru_m = '[bold cyan]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
############################
class Cek_Crack:
    def __init__(self):
        self.hsl_cp, self.hsl_ok = [], []
    
    def hasil(self):
        prints(Panel(f"""[{biru_m}01{hapus}] check hasil crack ok
[{biru_m}02{hapus}] check hasil crack cp
[{biru_m}03{hapus}] hapus hasil crack
[{merah}04{hapus}] kembali ke menu awal"""))
        xz = input(f"  [{M}?{N}]  input: ")
        if xz in[""]:
            print("");prints(Panel(f"😡 jangan kosong"));time.sleep(3);self.hasil()
        elif xz in["1", "01"]:
            try:
                dirs = os.listdir("results/OK")
                for i in dirs:
                    self.hsl_ok.append(i)
            except:pass
            if len(self.hsl_ok)==0:
                prints(Panel(f"🙁 {merah}tidak ada file yang mau di cek{hapus}"));exit()
            else:
                self.xa = {}
                self.xx = 0
                prints(Panel(f"       HASIL {hijau}OK {hapus}YANG TERSIMPAN DI FOLDER ANDA"))
                for ini in self.hsl_ok:
                    try:fi1 = open(f"results/OK/{ini}").readlines()
                    except:continue
                    self.xx+=1
                    if self.xx<100:
                        nom ="0"+str(self.xx)
                        self.xa.update({str(self.xx):str(ini)})
                        self.xa.update({nom:str(self.xx)})
                        print(f"  [{O}{nom}{N}] {ini} -> {H}{str(len(fi1))}{N}")
                    else:
                        self.xa.update({str(self.xx):str(ini)})
                        print(f"  [{O}{nom}{N}] {ini} -> {H}{str(len(fi1))}{N}")
                prints(Panel(f"         {biru_m}SILAHKAN PILIH NOMOR YANG MAU ANDA CEK{hapus}"))
                file = input(f"  [{M}?{N}] nomor : ")
                try:ajg = self.xa[file]
                except KeyError:
                    prints(Panel(f"😡 file {merah}{file}{hapus} tidak ada cek nomor nya pler"));exit()
                nm_file = ajg.replace("-", " ")
                hps_nm  = nm_file.replace(".txt", "").replace("OK", "")
                total = open(f"results/OK/{ajg}", "r").readlines()
                prints(Panel(f"[{biru_m}•{hapus}] Hasil crack pada tanggal:{hijau}{hps_nm}{hapus} total: [bold blue]{len(total)}[/]"))
                for ha in total:
                    kontol = ha.replace("\n","")
                    titid  = kontol.replace(" [✓] ","  \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ")
                    print(f"{titid}{N}");time.sleep(0.03)
                prints(Panel(f"             {hijau}PROSES MENGECEK HASIL SELESAI{hapus}"))
                input(f"   [ {O}KEMBALI{N} ] ");tt.Brute().moch_yayan()
        elif xz in["2", "02"]:
            try:
                xxx = os.listdir("results/CP")
                for z in xxx:
                    self.hsl_cp.append(z)
            except:pass
            if len(self.hsl_cp)==0:
                prints(Panel(f"🙁 {merah}tidak ada file yang mau di cek{hapus}"));exit()
            else:
                self.xa = {}
                self.xx = 0
                prints(Panel(f"       HASIL {kuning}CP {hapus}YANG TERSIMPAN DI FOLDER ANDA"))
                for tod in self.hsl_cp:
                    try:fi2 = open(f"results/CP/{tod}").readlines()
                    except:continue
                    self.xx+=1
                    if self.xx<100:
                        nom ="0"+str(self.xx)
                        self.xa.update({str(self.xx):str(tod)})
                        self.xa.update({nom:str(self.xx)})
                        print(f"  [{O}{nom}{N}] {tod} -> {H}{str(len(fi2))}{N}")
                    else:
                        self.xa.update({str(self.xx):str(tod)})
                        print(f"  [{O}{nom}{N}] {tod} -> {H}{str(len(fi2))}{N}")
                prints(Panel(f"         {biru_m}SILAHKAN PILIH NOMOR YANG MAU ANDA CEK{hapus}"))
                file = input(f"  [{M}?{N}] nomor : ")
                try:ajg = self.xa[file]
                except KeyError:
                    prints(Panel(f"😡 file {merah}{file}{hapus} tidak ada cek nomor nya pler"));exit()
                nm_file = ajg.replace("-", " ")
                hps_nm  = nm_file.replace(".txt", "").replace("CP", "")
                total = open(f"results/CP/{ajg}", "r").readlines()
                prints(Panel(f"[{biru_m}•{hapus}] Hasil crack pada tanggal:{hijau}{hps_nm}{hapus} total: [bold blue]{len(total)}[/]"))
                for ha in total:
                    kontol = ha.replace("\n","")
                    titid  = kontol.replace(" [×] ", "  \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                    print(f"{titid}{N}");time.sleep(0.03)
                prints(Panel(f"             {kuning}PROSES MENGECEK HASIL SELESAI{hapus}"))
                input(f"   [ {O}KEMBALI{N} ] ");tt.Brute().moch_yayan()
        elif xz in["3","03"]:
            prints(Panel(f"""[{biru_m}01{hapus}] hapus hasil ok
[{biru_m}02{hapus}] hapus hasil cp
[{biru_m}03{hapus}] kembali""", title=f"{merah}HAPUS HASIL CRACK{hapus}"))
            pil = input("  [?] pilih: ")
            if pil in ["1", "01"]:
                try:os.remove("results/OK")
                except:pass
                try:os.mkdir("results/OK")
                except:pass
                prints(Panel(f"[{hijau}✓{hapus}] berhasil menghapus semua hasil ok."));input(f"   [ {O}KEMBALI{N} ] ");tt.Brute().moch_yayan()
            elif pil in ["2", "02"]:
                try:os.remove("results/CP")
                except:pass
                try:os.mkdir("results/CP")
                except:pass
                prints(Panel(f"[{hijau}✓{hapus}] berhasil menghapus semua hasil cp."));input(f"   [ {O}KEMBALI{N} ] ");tt.Brute().moch_yayan()
            elif pil in ["3", "03"]:
                self.hasil()
            else:
                print("");prints(Panel(f"😡 memu [bold red]{pil}[/] tidak ada, cek menu nya!"));time.sleep(3);self.hasil()
        elif xz in["4","04"]:
            tt.Brute().moch_yayan()
        else:
            print("");prints(Panel(f"😡 memu [bold red]{xz}[/] tidak ada, cek menu nya!"));time.sleep(3);self.hasil()
