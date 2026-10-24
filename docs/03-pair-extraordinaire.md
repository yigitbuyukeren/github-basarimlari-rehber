# 3. Pair Extraordinaire: ortak yazarlı commit

Şartı: **`Co-authored-by` satırı olan bir commit'in bulunduğu PR merge edilsin.** İlk eşik 1 PR'dır. Gerçek bir
ortak yazar gerekir: arkadaşın, bir iş arkadaşın ya da birlikte çalıştığın biri.

> [!WARNING]
> İkinci bir hesap açıp kendini ortak yazar olarak yazma. Bu, GitHub kurallarına aykırıdır. Ortak yazarın
> gerçekten katkısı olmalı ve adının yazılmasını bilmeli.

## Adım 1: Ortak yazarın bilgisini bul

Ortak yazarın GitHub kullanıcı adı `ornek` olsun. Sayısal kimliğini şöyle öğren:

```bash
gh api users/ornek --jq '.id'
```

Çıkan sayı `12345678` ise ortak yazarın GitHub'a bağlı gizli e-postası `12345678+ornek@users.noreply.github.com` olur.
Ortak yazar kendi e-postasını biliyorsa onu da kullanabilir; adres hesabına bağlı olmalıdır.

## Adım 2: Commit mesajına satırı ekle

`Co-authored-by` satırı, mesajın **en sonunda ve bir boş satırdan sonra** gelmeli:

```bash
git switch -c ortak-calisma
echo "- Bu satırı birlikte yazdık." >> README.md
git add README.md
git commit -m "Ortak çalışma notu eklendi" -m "Co-authored-by: Ornek Kisi <12345678+ornek@users.noreply.github.com>"
```

İki `-m` bayrağı git'te mesajı iki paragraf yapar, aralarına boş satır koyar. Web arayüzünde commit
yazıyorsan açıklama kutusunun son satırına aynı satırı yaz.

## Adım 3: PR aç ve merge et

```bash
git push -u origin ortak-calisma
gh pr create --fill
gh pr merge --merge --delete-branch
```

Burada **Squash** yerine **Merge commit** (`--merge`) ya da **Rebase** (`--rebase`) kullanmak, ortak yazar
bilgisinin commit'te olduğundan emin olmanın en kolay yoludur.

## Kontrol

GitHub'da commit'e bak: iki profil resmi görünüyorsa satır doğru işlenmiş demektir. Yalnızca senin resmin
varsa e-posta adresi ortak yazarın hesabına bağlı değildir ya da satır boş satırdan sonra yazılmamıştır.

## Daha yüksek seviyeler

Bronz 10, gümüş 24, altın 48 PR ister. Bunun yolu, düzenli çalıştığın biriyle (proje arkadaşı, ekip) her
PR'a `Co-authored-by` eklemektir. Yapay şekilde şişirmeye çalışma.

**Sonraki:** [4. Public Sponsor](04-public-sponsor.md)
