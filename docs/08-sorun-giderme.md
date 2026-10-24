# 8. Sorun giderme

## Rozet profilimde görünmüyor

1. **24 saate kadar bekle.** Sayaçlar anında güncellenmez.
2. **Achievements kutusu açık mı?** *Settings → Public profile → Achievements*.
3. **PR'ı merge ettin mi?** Pull Shark ve Pair Extraordinaire yalnızca merge edilmiş PR'ı sayar; kapatılan
   (merge edilmemiş) PR sayılmaz.
4. **Repo public mi?** Private repo etkinliği için *Private contributions* kutusu açık olmalı.
5. **Commit e-postası hesabına bağlı mı?** *Settings → Emails* sayfasında adres görünmeli.
6. **Doğru hesabı mı kullanıyorsun?** `gh auth status` ve `git config user.email` çıktılarına bak.

## YOLO gelmedi

PR'ı merge ederken hiçbir review olmamalı. Kendi PR'ını "Approve" etmiş olmanı GitHub zaten engeller ama
yorum bırakmış (review comment) olabilirsin; sade bir PR aç ve review'suz merge et.

## Quickdraw gelmedi

Issue'yu açtığın andan itibaren 5 dakikayı geçmiş olabilir. Yeni bir issue aç, açar açmaz kapat. Başka bir
arkadaşının PR'ını kapatma, kendi issue'nu kullan.

## Pair Extraordinaire gelmedi

- `Co-authored-by` satırı mesajın **sonunda ve bir boş satırdan sonra** mı?
- E-posta, ortak yazarın GitHub hesabına bağlı mı? Gizli adres için sayısal kimliği (`gh api users/<ad> --jq .id`)
  kullan.
- PR'ı `Squash` ile mi merge ettin? `Merge commit` ya da `Rebase` ile dene.

## Hâlâ olmuyor mu

- Başarımların kuralları GitHub tarafından değiştirilebilir; bu rehberdeki eşikler topluluk kaynaklarından
  derlendi (README'nin sonundaki kaynaklar).
- Bir hata bulduysan ya da bir şey değiştiyse [issue aç](https://github.com/yigitbuyukeren/github-basarimlari-rehber/issues/new).

[← Başa dön](../README.md)
