# Katkı rehberi

Rehberdeki bir bilgi eskidiyse ya da yanlışsa katkın çok değerli.

## Ne tür katkılar işe yarar

- Bir başarımın şartı ya da eşiği değiştiyse: güncel kaynakla birlikte düzeltme.
- Kaynaklarda çelişen bir bilgiyi kendi denemenle doğrulamak (hangi tarihte, nasıl denediğini yaz).
- Yazım hataları, bozuk bağlantılar, daha anlaşılır anlatım.
- Komutlarda işletim sistemine özgü farklar (Windows, Linux).

## Nasıl katkı verilir

1. Repoyu fork'la ve bir branch aç.
2. Değişikliği yap. Türkçe yaz, mevcut sayfaların sade dilini koru.
3. Bir bilgiyi değiştiriyorsan kaynağı PR açıklamasına ekle.
4. `python3 tools/check_links.py` ile yerel Markdown bağlantılarını, ayrıca değişen sayfadaki dış bağlantıları ve görselleri kontrol et; boşluk hataları için `git diff --check` çalıştır.
5. PR gönder.

## Yapılmaması gerekenler

- Kaynağı belirtilmeyen eşik ya da şart eklemek.
- Hesap şişirmeyi, sahte yıldızı ya da kuralları aşmayı öneren içerik.
- Kişisel hesap bilgisi, parola ya da token paylaşmak.
