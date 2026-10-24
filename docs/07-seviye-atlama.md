# 7. Bronz, gümüş ve altın

Seviyeli dört başarımın eşikleri:

| Başarım | Varsayılan | Bronz | Gümüş | Altın |
|---|---:|---:|---:|---:|
| 🦈 Pull Shark (merge edilen PR) | 2 | 16 | 128 | 1024 |
| ⭐ Starstruck (tek repoda yıldız) | 16 | 128 | 512 | 4096 |
| 👥 Pair Extraordinaire (ortak yazarlı merge edilmiş PR) | 1 | 10 | 24 | 48 |
| 🧠 Galaxy Brain (kabul edilen cevap) | 2 | 8 | 16 | 32 |

## Pull Shark'ı dürüstçe büyütmek

16 PR'a ulaşmanın en kalıcı yolu açık kaynağa gerçekten katkı vermektir:

1. Kullandığın bir projede `good first issue` ya da `help wanted` etiketli issue'lara bak:
   ```bash
   gh search issues --label "good first issue" --state open --language javascript
   ```
2. Projenin `CONTRIBUTING.md` dosyasını oku, kurallara uy.
3. Yazım hatası, eksik dokümantasyon, bozuk bağlantı ya da küçük bir hata düzeltmesi gibi gerçek bir iş seç.
4. Fork'la, branch aç, düzelt, PR gönder.

```bash
gh repo fork sahip/proje --clone
cd proje
git switch -c yazim-hatasi
# düzelt, sonra
git commit -am "Dokümantasyondaki yazım hatası düzeltildi"
git push -u origin yazim-hatasi
gh pr create --fill
```

Kendi reponda sürekli küçük PR açıp merge etmek de saydığı için çok kişi bunu yapıyor, ama bir noktadan sonra
yapay görünür. Kural: her PR bir şeyi iyileştirsin.

## Aşırıya kaçma

- Tek bir değişikliği parçalara bölüp çok PR'a yaymak.
- Başkalarının reposuna anlamsız "Update README.md" PR'ları yağdırmak. Bakımcılar spam olarak işaretler,
  yeni katkıcıları kısıtlayan kurallar da bu yüzden var.
- Rozet eşiklerine ulaşmak için hesabın dışında bir yardım örgütlemek.

## İpucu: ilerlemeni takip et

```bash
gh search prs --author @me --merged --limit 100 --json number --jq 'length'
```

Bu komut merge edilmiş PR'larının kabaca sayısını verir (`@me` giriş yapan hesaptır).

**Sonraki:** [8. Sorun giderme](08-sorun-giderme.md)
