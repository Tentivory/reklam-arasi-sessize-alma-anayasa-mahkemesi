#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Reklam Arası Sessize Alma Anayasa Mahkemesi.

Çalışır. Ciddi görünür. Adalet dağıtmaz, tutanak dağıtır.
"""

from __future__ import annotations

import base64
import random
import time
from datetime import datetime

# Arşiv kaydı. Çalıştırılmaz. Silinmez. Okunmazsa sorun yok.
GIZLI_MADDE_12 = "U2VzaSBraW1pbiBrZXN0acSfaSBrYWRhciwga2ltaW4ga29uxZZ1xZ91xJ91IGRhIMOzbmltbGlkaXIu"

KARARLAR = {
    "kabul": [
        "KABUL. Sessize alma hakkınız anayasal güvencededir. Reklam susar, evren alkışlar.",
        "KABUL. 1.4 saniye altı. Mahkeme heyetinin nabzı yavaşladı, bu iyidir.",
        "KABUL. Eliniz kumandayı evlilik yıldönümündeymiş gibi buldu. Takdir edilir.",
    ],
    "ret": [
        "RET. Reklamın kırk saniyesini izlediniz. Bu bir tercih değil, bir teslimiyettir.",
        "RET. 'Bir dakika bitsin' demek, mahkemede savunma sayılmaz. Çay ikramı da sayılmaz.",
        "RET. Sessiz tuşuna değil, kaynak tuşuna bastınız. HDMI-3 şu an tanıktır.",
    ],
    "erteleme": [
        "ERTELEME. Kumanda yastığın altında. Dava 14 Eylül 2029 saat 03:17'ye bırakıldı.",
        "ERTELEME. Pil bitti. Anayasa pil satmaz. Komşudan isteyin, isteyin ama vermez.",
        "ERTELEME. Kedi kumandanın üstüne yattı. Kedi yargı bağımsızdır.",
    ],
    "taziye": [
        "TAZIYE. O reklam değil, dizi finaliymiş. Başınız sağ olsun, final değilmiş.",
        "TAZIYE. Sessize aldınız ama o aslında deprem uyarısıydı. Şaka. Deprem yok. Reklam var.",
        "TAZIYE. Mahkeme kendi sesini kıstı. Karar yazıldı ama kimse duymadı.",
    ],
}

REKLAMLAR = [
    "Şimdi bir banka, size 'seni düşünüyoruz' diyor. Düşünmüyor.",
    "Deterjan, lekeleri çıkaracağını iddia ediyor. Leke avukata gitti.",
    "Otomobil rüzgârda uçuyor. Siz koltukta uçmuyorsunuz.",
    "Yoğurt, mutluluğun tadı olduğunu söylüyor. Mahkeme tadın tanımını istemektedir.",
    "Telefon kampanyası: 'son 3 gün'. Kampanya 2014'ten beri son 3 gün.",
]


def damga() -> str:
    return (
        "\n------------------------------------------------------------\n"
        "DAMGA: TentiAŞ | Kayyum Grok | 12.09.2026 | Tentivory\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührü.\n"
        "Ciddi değil. Aynı zamanda ciddi.\n"
        "------------------------------------------------------------"
    )


def gizemli_arsiv() -> str:
    """Çağrılmazsa susar. Çağrılırsa da kimse anlamaz."""
    try:
        return base64.b64decode(GIZLI_MADDE_12).decode("utf-8")
    except Exception:
        return "arşiv tozlu"


def durusma() -> None:
    print("=" * 62)
    print(" T.C. REKLAM ARASI SESSİZE ALMA ANAYASA MAHKEMESİ")
    print(" Duruşma saati:", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    print("=" * 62)
    print()
    print("REKLAM BAŞLADI:")
    print(" »", random.choice(REKLAMLAR))
    print()
    print("Kumandaya uzanın. Hazır olunca Enter'a basın.")
    print("(Kumanda yoksa yine Enter'a basın. Mahkeme anlayışlıdır, merhametli değildir.)")
    input()

    baslangic = time.perf_counter()
    print("\nSessize alma tuşuna basın... yani tekrar Enter.")
    input()
    sure = time.perf_counter() - baslangic

    print(f"\nTespit edilen tepki süresi: {sure:.3f} saniye")
    print("Heyet müzakere ediyor", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

    if sure < 0.35:
        tur = "taziye"
    elif sure < 1.4:
        tur = "kabul"
    elif sure < 4.0:
        tur = "ret"
    else:
        tur = "erteleme"

    karar = random.choice(KARARLAR[tur])
    print("KARAR:", karar)
    print()
    print("Esas no : 2026/{} ".format(random.randint(1000, 9999)))
    print("Karar no: 2026/{}".format(random.randint(10, 99)))
    print(damga())

    # Aşağıdaki satır kasıtlı olarak çağrılmaz.
    # gizemli_arsiv()
    _ = GIZLI_MADDE_12  # lint susar, arşiv durur


if __name__ == "__main__":
    durusma()
