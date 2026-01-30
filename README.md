# Uber Data Lakehouse: Medallion Architecture with PySpark and dbt Cloud

Bu repository, bulut tabanlı büyük veri ekosistemlerinde verinin ham
formdan analitik bir varlığa dönüşüm sürecini yöneten, ölçeklenebilir ve
dinamik bir veri işleme hattı (pipeline) tasarımıdır. Proje kapsamında
Uber simüle edilmiş veri seti kullanılarak uçtan uca bir **Data
Lakehouse mimarisi** inşa edilmiştir.

------------------------------------------------------------------------

## 1. Proje Genel Bakış

Geleneksel ETL süreçlerinin aksine, bu çalışma **Nesne Yönelimli
Programlama (OOP)** ve **dinamik şablon dilleri (Jinja)** kullanarak;

-   Bakım maliyeti düşük\
-   Hata toleransı yüksek\
-   Artımlı (incremental) veri işleme yeteneğine sahip

modern bir veri platformu sunar.

### 1.1 Temel Teknik Bileşenler

-   **Mimari:** Üç katmanlı Medallion (Bronze, Silver, Gold) mimarisi\
-   **Veri İşleme:** Apache Spark (PySpark) Structured Streaming\
-   **Modelleme:** dbt Cloud ile boyutsal modelleme (Star Schema)\
-   **Tarihçe Yönetimi:** SCD Type 2 (Slowly Changing Dimensions) ve
    Snapshots

------------------------------------------------------------------------

## 2. Sistem Mimarisi (Medallion Architecture)

Veri kalitesi ve güvenilirliği aşağıda belirtilen üç aşamalı yapı ile
optimize edilmektedir:

### Bronze Layer (Raw)

Kaynak sistemlerden gelen verilerin **Delta formatında**, yapısal
değişikliğe uğratılmadan saklandığı ham veri katmanıdır.

### Silver Layer (Validated)

-   Veri temizleme\
-   Tekilleştirme (Deduplication)\
-   İş kuralları uygulama

işlemlerinin yapıldığı zenginleştirilmiş veri katmanıdır.

### Gold Layer (Analytics)

İş zekası (BI) ve raporlama araçları için optimize edilmiş, tarihsel
boyut yönetimi uygulanmış nihai analiz katmanıdır.

------------------------------------------------------------------------

## 3. Repository Hiyerarşisi

``` text
├── databricks_notebooks/
│   ├── bronze_ingestion
│   └── silver_refinement
│
├── dbt_project/
│   ├── models
│   ├── snapshots
│   ├── macros
│   └── dbt_project.yml
│
└── README.md
```

------------------------------------------------------------------------

## 4. Teknik Uygulama Analizi

### 4.1 Dinamik Veri Entegrasyonu (PySpark)

Projede geliştirilen dinamik ingestion mekanizması tablo listesi
üzerinden iterasyon yaparak şema yönetimini ve veri alımını
otomatikleştirir.\
Checkpointing mekanizması sayesinde sistem kesintilerinde veri
tutarlılığı korunur.

------------------------------------------------------------------------

### 4.2 dbt Modelleme ve Veri Soy Ağacı (Lineage)

dbt Cloud entegrasyonu ile:

-   Veri soy ağacı uçtan uca izlenebilir\
-   Bağımlılıklar merkezi yönetilir\
-   Veri yönetişimi güçlendirilir

------------------------------------------------------------------------

### 4.3 Yavaş Değişen Boyutlar (SCD Type 2)

-   dbt Snapshots kullanılarak tarihsel değişimler tutulur\
-   `dbt_valid_from` ve `dbt_valid_to` kolonları ile zaman bütünlüğü
    sağlanır\
-   Güncel kayıtlar için **9999-12-31** stratejisi uygulanır

------------------------------------------------------------------------

## 5. Kurulum ve Dağıtım

### 5.1 Databricks

1.  `databricks_notebooks` klasörünü Workspace'e yükleyin\
2.  Unity Catalog yetkilendirmelerini yapılandırın

------------------------------------------------------------------------

### 5.2 dbt Cloud

1.  GitHub repository bağlantısını yapın\
2.  Environment variable ayarlarını girin

------------------------------------------------------------------------

### 5.3 Çalıştırma Sırası

1.  Bronze Ingestion\
2.  Silver Refinement\
3.  Gold katmanı için:

``` bash
dbt build
```

------------------------------------------------------------------------

## 6. İletişim

**Geliştiren:** Abdulsamet Duran\
**E-posta:** asametdurann@gmail.com
