# 2. Kolay üç rozet: Quickdraw, YOLO, Pull Shark

Bu üçü yalnızca **kendi reponla** alınır, başka kimsenin onayı gerekmez. Hepsi yaklaşık 15 dakikada bitebilir.

| Rozet | Kısaca | Bu sayfada |
|---|---|---|
| ⚡ Quickdraw | Bir issue'yu açtıktan 5 dakika içinde kapat | Adım 2 |
| 🤠 YOLO | Review'suz bir PR'ı merge et | Adım 3 |
| 🦈 Pull Shark | 2 PR'ın merge edilsin | Adım 3 ve 4 |

> [!IMPORTANT]
> Anlamsız değişiklikle PR açma. Gerçekten işe yarayan küçük bir şey yap: bir not defteri, bir komut listesi,
> bir çalışma günlüğü. Aşağıdaki örnek bunu "çalışma defteri" reposuyla gösterir.

## Adım 1: Kendi reponu aç

```bash
gh repo create calisma-defteri --public --add-readme --clone
cd calisma-defteri
```

Repo **public** olsun; rozetler en güvenilir biçimde herkese açık repolardaki işle sayılır.
Aynı işi web'de yapmak için: *github.com → New repository → "Add a README file" → Create*.

## Adım 2: Quickdraw (issue aç, 5 dakikada kapat)

Kural: bir issue ya da pull request'i **açtıktan sonra 5 dakika içinde kapatmak**. En sorunsuz yol issue:

```bash
gh issue create --title "Çalışma günlüğü bölümü ekle" --body "README'ye günlük için bir bölüm eklenecek."
# Çıktıdaki sayı issue numarasıdır (örneğin #1)
gh issue close 1 --comment "Planlandı, PR ile yapılacak."
```

Süre sayacı issue açıldığı anda başlar: iki komutu arka arkaya çalıştır. Web'de: *Issues → New issue →
Submit new issue*, hemen ardından **Close issue**.

## Adım 3: Pull Shark için ilk PR, YOLO ile birlikte

YOLO'nun şartı: pull request'i **hiç review almadan merge etmek**. Kendi reponda zaten kimse review
yazmayacağı için sorunsuzdur. Bir PR ile hem YOLO hem Pull Shark sayacının ilk adımını almış olursun.

```bash
git switch -c gunluk-bolumu
printf '\n## Çalışma günlüğü\n\n- İlk kayıt: GitHub başarımlarını öğreniyorum.\n' >> README.md
git add README.md
git commit -m "Çalışma günlüğü bölümü eklendi"
git push -u origin gunluk-bolumu
gh pr create --fill
gh pr merge --squash --delete-branch
git switch main && git pull
```

`gh pr merge` hangi yöntemle birleştireceğini sorarsa **Squash** seç. Web'de: *Compare & pull request →
Create pull request → Squash and merge → Confirm*. Hiç "Approve" ya da "Request changes" yazılmadığından
emin ol.

> [!NOTE]
> Repoda "Require a pull request before merging" ya da zorunlu review kuralı açıksa kendi PR'ını merge
> edemezsin. Yeni bir repoda bu kurallar kapalıdır; dokunma.

## Adım 4: Pull Shark için ikinci PR

Pull Shark'ın ilk eşiği **2 merge edilmiş PR**. İkincisini, farklı ve gerçek bir değişiklikle aç:

```bash
git switch -c komut-listesi
printf '\n## Sık kullandığım komutlar\n\n- `git status`: durumu göster\n- `git log --oneline`: geçmişi kısa göster\n' >> README.md
git add README.md
git commit -m "Sık kullanılan komutlar eklendi"
git push -u origin komut-listesi
gh pr create --fill
gh pr merge --squash --delete-branch
git switch main && git pull
```

## Kontrol listesi

- [ ] Bir issue 5 dakika içinde kapandı (Quickdraw)
- [ ] En az bir PR review'suz merge edildi (YOLO)
- [ ] İki PR **merge** edildi, yalnızca kapatılmadı (Pull Shark)

Rozetlerin profilinde görünmesi birkaç saat, bazen 24 saate kadar sürebilir. Görünmezse
[8. Sorun giderme](08-sorun-giderme.md) sayfasına bak.

**Sonraki:** [3. Pair Extraordinaire](03-pair-extraordinaire.md)
