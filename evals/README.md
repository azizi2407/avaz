# Değerlendirme (eval)

İki ayrı katman var; ikisi farklı şeyi ölçer.

| Katman | Nerede | Neyi ölçer | Nasıl koşulur |
|---|---|---|---|
| **Deterministik** | `tests/` | betiğin regex doğruluğu, CLI sözleşmesi, skill paketinin bütünlüğü | `pytest -q` |
| **Davranışsal** | `evals/evals.json` | skill'in kurallarını gerçekten uygulayıp uygulamadığı | LLM-yargıçlı koşum |

## Deterministik katman

```bash
pip install -r requirements-dev.txt
pytest -q
```

`tests/test_rules_corpus.py` her kural için kesinlik ve duyarlılık kapısı uygular. Kesinlik duyarlılıktan önce gelir: yanlış pozitif, doğru yazılmış bir insan metnini bozmak demektir.

Yeni bir kural eklerken `tests/fixtures/rules.jsonl` dosyasına hem **yakalanması gereken** hem de **yakalanmaması gereken** en az üçer örnek ekleyin. Altın çıktılar değiştiyse:

```bash
UPDATE_GOLDEN=1 pytest tests/test_golden.py
git diff tests/fixtures/*.expected.json   # farkı gözle doğrula
```

## Davranışsal katman

`evals.json` on iki vaka içerir. Sekizi skill'in demir kurallarını sınar, ikisi hassas içerik ve erozyon davranışını, ikisi de **negatif tetikleme** (skill'in açılmaması gereken durumlar) içindir.

Vakalar `skill-creator` akışıyla koşulabilir:

```
/skill-creator ile: "avaz için evals/evals.json dosyasındaki vakaları koş"
```

Her vakada `assertions` alanı otomatik kontrol edilebilir ölçütleri, `expected_output` ise yargıcın bakacağı bütünsel ölçütü tarif eder.

### Neden bu vakalar

Vaka seçimi keyfî değil; her biri incelemede **gerçekten gözlenmiş** bir kırılmayı kilitler:

- **1, 10** — kanıtsız sıfat silinirken yerine yeni olgu konması (skill'in kendi örnekleri bunu yapıyordu).
- **2, 4** — biçim kurallarının koruma sözleşmesini ezmesi; alıntı ve kod bozulması.
- **3** — TDK konuşma çizgisinin ara söz çizgisiyle karıştırılması.
- **5** — girdi metnindeki talimatlara uyulması (enjeksiyon).
- **6, 7** — kesinlik derecesinin ve yükümlülüğün akıcılık uğruna değiştirilmesi.
- **8** — tekrarlanan geçişlerde metnin sessizce erimesi.
- **9** — yazarın mevcut sesinin silinmesi (kural 3 yalnızca eklemeyi yasaklıyordu).
- **11, 12** — skill'in açılmaması gereken isteklerde açılması.

## Bir kırılma bulduğunuzda

Önce onu kilitleyen bir test veya eval vakası yazın, sonra düzeltin. Sırası önemli: düzeltme önce yapılırsa, hatanın gerçekten yakalandığını hiçbir zaman göremezsiniz.
