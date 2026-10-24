# 1. Hazırlık

Rozetlerin çoğu için tek bir hesap, `git` ve GitHub'ın komut satırı aracı `gh` yeter. Bu sayfa kurulumu anlatır;
sonraki sayfalarda her komutu bu kurulumun üstüne yazıyoruz.

## Gerekenler

| Araç | Ne için | Kurulum |
|---|---|---|
| Git | Commit ve push | macOS: `xcode-select --install`, Windows: [git-scm.com](https://git-scm.com), Linux: paket yöneticin |
| GitHub CLI (`gh`) | Repo, issue ve PR'ı terminalden açmak | macOS: `brew install gh`, Windows: `winget install GitHub.cli`, Linux: [cli.github.com](https://cli.github.com) |
| GitHub hesabı | | [github.com/signup](https://github.com/signup) |

`gh` kullanmak şart değil: aşağıdaki her adımı github.com üzerinden tıklayarak da yapabilirsin. Komutlar
yalnızca daha hızlı olduğu için var.

## Giriş yap

```bash
gh auth login
```

Sorulara şunları ver: `GitHub.com`, `HTTPS`, `Login with a web browser`. Tarayıcıda çıkan kodu gir.
Kontrol:

```bash
gh auth status
```

## Git'e kim olduğunu söyle

Commit'lerin profilindeki katkı grafiğine yazılması için e-posta adresin GitHub hesabına bağlı olmalı.
E-postanı açığa çıkarmak istemiyorsan GitHub'ın verdiği gizli adresi kullan: *Settings → Emails →
"Keep my email addresses private"* (adres `ID+kullanici@users.noreply.github.com` biçimindedir).

```bash
git config --global user.name "Adın Soyadın"
git config --global user.email "ID+kullanici@users.noreply.github.com"
```

## Başarımlar profilinde görünsün

*Profil fotoğrafı → Settings → Public profile* sayfasında **Achievements** kutusunu işaretli bırak.
Özel (private) repolardaki işlerin de sayılmasını istersen aynı sayfada **Private contributions**
kutusunu aç. Bu ayarlar kapalıysa rozet kazansan bile profilinde görünmez.

## Güvenlik ve kurallar

- Tek kişi için tek hesap. İkinci bir hesap açıp kendi kendine PR, yıldız ya da yardım göndermek GitHub'ın
  kullanım şartlarına aykırıdır ve hesabın kısıtlanmasına yol açabilir.
- Başkasının reposunda yalnızca gerçek bir iş yap. Anlamsız commit, boş PR ya da toplu spam, hem rozet
  getirmeyebilir hem de seni engellettirir.
- Parola, token ya da özel anahtarı hiçbir repoya (public olanlara hiç) koyma.

**Sonraki:** [2. Kolay üç rozet](02-kolay-rozetler.md)
