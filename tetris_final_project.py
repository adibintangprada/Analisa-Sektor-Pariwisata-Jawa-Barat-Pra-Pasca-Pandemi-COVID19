from scipy import signal
from turtle import bgcolor
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Setting the Page Config
st.set_page_config(page_title="Analisa Sektor Pariwisata Jawa Barat Pra-Pasca Pandemi COVID19",
                   layout="wide",
                   menu_items={
                       "Get help":"mailto:adibintangprada@gmail.com",
                       "About":"https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19"
                   })


# Load the Datasets
# Kerugian Finansial Benua
url_kerugian_finansial_benua = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/kerugian_finansial_benua.csv?raw=true"
kerugian_finansial_benua = pd.read_csv(url_kerugian_finansial_benua)

# Akomodasi Wisata Jabar
url_akomodasi_wisata = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/akomodasi_wisata_summed.csv?raw=true"
akomodasi_wisata = pd.read_csv(url_akomodasi_wisata)

# Jasa Penunjang Wisata Jabar
url_jasa_penunjang = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/jasa_penunjang_wisata_summed.csv?raw=true"
jasa_penunjang = pd.read_csv(url_jasa_penunjang)

# Jumlah Wisatawan Jabar
url_jumlah_wisatawan_jabar = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/jumlah_wisatawan_jabar_summed.csv?raw=true"
jumlah_wisatawan_jabar = pd.read_csv(url_jumlah_wisatawan_jabar)

# Mobilitas Jabar
url_mobilitas_jabar = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/mobilitas_jabar_cleaned.csv?raw=true"
mobilitas_jabar = pd.read_csv(url_mobilitas_jabar)

# Objek Wisata Jabar
url_objek_wisata = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/objek_wisata_jabar_summed.csv?raw=true"
objek_wisata_jabar = pd.read_csv(url_objek_wisata)

# Pendapatan Wisata Jabar
url_pendapatan_wisata = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/pendapatan_wisata_jabar_summed.csv?raw=true"
pendapatan_wisata_jabar = pd.read_csv(url_pendapatan_wisata)

# Pengeluaran Wisatawan
url_pengeluaran_wisatawan = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/pengeluaran_wisatawan.csv?raw=true"
pengeluaran_wisatawan = pd.read_csv(url_pengeluaran_wisatawan)

# Sarana Wisata Jabar
url_sarana_wisata = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/tempat_hiburan_jabar.csv?raw=true"
sarana_wisata = pd.read_csv(url_sarana_wisata)

# Jumlah Wisatawan Indonesia
url_jumlah_wisatawan_indo = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/wisatawan_indonesia.csv?raw=true"
jumlah_wisatawan_indo = pd.read_csv(url_jumlah_wisatawan_indo)

# Jumlah Wisatawan Nusantara Pulau Jawa
url_jumlah_wisatawan_pulau_jawa = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/dataset/jumlah_wisatawan_nusantara_pulau_jawa.csv?raw=true"
jumlah_wisatawan_pulau_jawa = pd.read_csv(url_jumlah_wisatawan_pulau_jawa, sep=';')

# Load the Images (If Needed)
# Raja Ampat
url_raja_ampat = "https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19/blob/main/images/header.png?raw=true"


# Header Image dan Judul
st.image(url_raja_ampat)
st.title('Analisa Sektor Pariwisata Jawa Barat Pra-Pasca Pandemi COVID19', 
         anchor="https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19")
st.caption("Created by Adi Bintang Pradana")
st.caption("For more details visit: https://github.com/adibintangprada/Analisa-Sektor-Pariwisata-Jawa-Barat-Pra-Pasca-Pandemi-COVID19")

# Dampak Pandemi COVID19 Pada Sektor Pariwisata Dunia dan Indonesia
st.header("Dampak Pandemi COVID19 Pada Sektor Pariwisata Dunia dan Indonesia")
st.write("Pandemi COVID19 membuat dunia menghadapi situasi yang belum pernah terjadi sebelumnya dan menimbulkan banyak tantangan multi-dimensional yang harus dihadapi, tak terkecuali pada sektor pariwisata. Menurut **_United Nations World Tourism Organization (UNWTO)_**, sektor pariwisata adalah yang paling terpukul oleh pandemi COVID19. UNWTO memberikan catatan bahwa tahun 2020 adalah tahun terburuk bagi sektor pariwisata internasional.")
st.write("Menurut UNWTO World Tourism Barometer (Januari 2021), pada tahun 2020, statistik kedatangan wisatawan (turis) secara internasional mengalami **_penurunan sekitar 74 persen, yaitu dari 1,5 miliar USD pada tahun 2019 menjadi sekitar 381 juta USD pada tahun 2020._** Kerugian yang diakibatkan oleh penurunan kunjungan wisatawan ini mencapai **_sekitar 1,3 triliun USD_** dalam pengeluaran pariwisata internasional. Kerugian akibat pandemi Covid-19 ini **_setara dengan 11 kali kerugian akibat krisis global tahun 2009._**")

# Perkembangan Sektor Penerbangan Saat Pandemi COVID19
st.subheader("Perkembangan Sektor Penerbangan Saat Pandemi COVID19")

# Dividing Into 2 Columns
col1, col2 = st.columns(2)

with col1:
    st.write("Sektor transportasi adalah salah satu sektor yang erat kaitannya dengan pariwisata, contohnya adalah sektor penerbangan. **_International Civil Aviation Organization (ICAO)_** menyatakan bahwa tahun 2020 adalah tahun terburuk bagi dunia penerbangan dengan runtuhnya permintaan perjalanan secara global.")
    st.write("Total penumpang tahun 2020 **_turun sebesar 60 persen_** akibat hantaman pandemi Covid-19, **_yaitu dari 4,5 miliar pada tahun 2019 menjadi sebesar 2,7 miliar pada tahun 2020._** Akibat penurunan lalu lintas udara, kerugian finansial maskapai diperkirakan mencapai **_USD 370 miliar,_** dengan kerugian terbesar **_di Asia/Pasifik yaitu sebesar 120 juta USD._** (lihat grafik di samping)")
    st.write("Indonesia sendiri termasuk ke dalam negara yang mengalami kerugian besar pada sektor penerbangan saat pandemi COVID19 menghantam. Dengan akses masuk yang terbatas, apakah jumlah wisatawan di Indonesia terpengaruh?")
    
with col2:
    kerugian_finansial_benua = kerugian_finansial_benua.sort_values(by=['loss'], ascending=True)
    fig = px.bar(
    kerugian_finansial_benua, 
    x='country', 
    y='loss',
    text_auto=True,
    title='Kerugian Yang Dialami Sektor Pariwisata Internasional (Dalam Juta Dolar US)',
    color_discrete_sequence=['red']*6,
    labels={
        "country":"Negara",
        "loss":"Kerugian"
    })
    fig.update_layout(
    hoverlabel=dict(
        bgcolor='white'
    ))
    st.plotly_chart(fig, use_container_width=True)
    st.caption("_Sumber: Tourism Satellite Account Indonesia 2016-2020, Kemenparekraf_")

# Perkembangan Wisatawan di Indonesia
st.subheader("Perkembangan Wisatawan di Indonesia")

# Dividing Into 2 Columns
col1, col2 = st.columns(2)

with col1:
    fig = px.line(
        jumlah_wisatawan_indo,
        x='tahun',
        y='jumlah',
        color='jenis_wisatawan',
        markers=True,
        title="Perkembangan Jumlah Wisatawan di Indonesia (Dalam Juta Orang)",
        color_discrete_map={
            "NUSANTARA":"#77E9C3",
            "MANCANEGARA":"#41B1F1"
        },
        category_orders={
            "jenis_wisatawan": ["NUSANTARA","MANCANEGARA"]
        },
        labels={
            "tahun":"Tahun",
            "jumlah":"Jumlah",
            "jenis_wisatawan":"Jenis Wisatawan"
        })
    fig.update_layout(
        hoverlabel=dict(
            bgcolor='white'
        ))
    fig.update_traces(mode="markers+lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("_Sumber: Tourism Satellite Account Indonesia 2016-2020, Kemenparekraf_")

with col2:
    st.write("Jumlah kunjungan wisatawan mancanegara ke Indonesia sebelum tahun 2020 menunjukkan pertumbuhan yang positif. Jumlah kunjungan tertinggi tercatat pada tahun 2019, yaitu sebesar **_16,11 juta orang._** Namun, pada tahun 2020 terjadi **_penurunan hampir 75 persen_** jika dibandingkan tahun sebelumnya.")
    st.write("Begitu juga dengan kunjungan wisatawan nusantara mengalami trend kenaikan yang positif sebelum tahun 2020, yang mana puncaknya adalah pada tahun 2019 sebesar **_722,16 juta orang._**  Pada tahun 2020 terjadi **_penurunan sebesar 28,19 persen_** jika dibandingkan tahun sebelumnya.")
    st.write("Dengan jumlah wisatawan baik nusantara maupun amncanegara yang turun secara signifikan pada tahun 2020, bagaimana pengaruhnya pada pengeluaran wisatawan?")

# Perkembangan Pengeluaran Wisatawan di Indonesia
st.subheader("Perkembangan Pengeluaran Wisatawan di Indonesia")

# Creating the Graph
fig = px.bar(pengeluaran_wisatawan,
             x="tahun",
             y="jumlah",
             color="jenis_wisatawan",
             title="Pengeluaran Wisatawan di Indonesia (Dalam Triliun Rupiah)",
             text_auto=True,
             category_orders={
                 "jenis_wisatawan": ["NUSANTARA", "MANCANEGARA"]
             },
             labels={
                 "tahun":"Tahun",
                 "jumlah":"Jumlah",
                 "jenis_wisatawan":"Jenis Wisatawan"
             },
             color_discrete_map={
            "NUSANTARA":"#77E9C3",
            "MANCANEGARA":"#41B1F1"}
             )
fig.update_layout(
    hoverlabel=dict(
        bgcolor='white'))
st.plotly_chart(fig, use_container_width=True)
st.caption("_Sumber: Tourism Satellite Account Indonesia 2016-2020, Kemenparekraf_")

# Adding the detail paragraph
st.write("Pengeluaran wisatawan di Indonesia dapat dikategorikan menjadi dua yaitu pengeluaran yang dilakukan oleh **_wisatawan mancanegara_** dan **_wisatawan nusantara._** Kedua jenis wisatawan tersebut sama-sama memiliki tren yang positif dari tahun 2016 hingga 2019. Akan tetapi terjadi **_kontraksi sebesar 74,55 persen_** pada wisatawan mancanegara dan **_53,64 persen_** pada wisatawan nusantara. Hal ini disebabkan karena saat pandemi COVID19, banyak akses penerbangan internasional dibatasi dan mobilitas dalam negeri pun turut dibatasi.")


# Perkembangan Sektor Pariwisata Jawa Barat
st.header("Perkembangan Sektor Pariwisata Jawa Barat")
st.write("Saat pandemi COVID19 terjadi di Indonesia, berbagai upaya pembatasan sosial dilakukan oleh pemerintah untuk menekan laju penularan virus. Hal ini berimbas pada turunnya berbagai aspek pariwisata seperti yang telah dijelaskan di bagian sebelumnya. Berbagai pembatasan tersebut berimbas pada **_meruginya sektor penerbangan dan turunnya wisatawan baik mancanegara maupun nusantara di Indonesia._**")
st.write("Setelah mengetahui fakta tersebut, bagaimanakah keadaan sektor pariwisata **_Jawa Barat_**? Jika terdampak, seberapa parah dampaknya?")

# Tren Jumlah Wisatawan di Jawa Barat
st.subheader("Tren Jumlah Wisatawan di Jawa Barat")

# Dividing Into 2 Columns
col1, col2 = st.columns(2)

with col1:
    st.write("Menurut data jumlah wisatawan pada Open Data Jabar, wisatawan nusantara mengalami **_penurunan mulai tahun 2019 dibanding tahun sebelumnya._** Pada **_tahun 2019 mengalami penurunan sebesar 76.84 persen_** dibanding tahun sebelumnya. **_Tahun 2020 mengalami penurunan sebesar 49.8 persen, tetapi tahun 2021 jumlah wisatawan nusantara mengalami kenaikan sebesar 22.62 persen._** Jadi, Jawa Barat memang mengalami penurunan wisatawan pada tahun 2020. Tetapi, terlepas dari pembatasan sosial yang ketat tahun 2021 tetap ada kenaikan pada jumlah wisatawan nusantara di Jawa Barat.")
    st.write("Tetapi, jumlah wisatawan nusantara di Jawa Barat tetap mengalami penurunan sebelum pandemi terjadi. Jadi bisa diasumsikan bahwa ada penyebab lain yang membuat jumlah wisatawan nusantara turun. Pada report ini belum ada data yang mendukung asumsi tersebut.")
    st.write("Sedangkan wisatawan mancanegara mengalami **_penurunan pada tahun 2020 sebesar 82.8 persen dan tahun 2021 sebesar 95.5 persen._** Pembatasan akses internasional yang ketat menyebabkan jumlah wisatawan mancanegara turun secara signifikan")

with col2:
    fig = px.line(
        jumlah_wisatawan_jabar,
        x='tahun',
        y='f0_',       
        markers=True,
        title="Jumlah Wisatawan di Jawa Barat 2014-2021",
        color="jenis_wisatawan",
        color_discrete_map={
            "NUSANTARA":"#77E9C3",
            "MANCANEGARA":"#41B1F1"
        },
        category_orders={
            "jenis_wisatawan": ["NUSANTARA","MANCANEGARA"]
        },
        labels={
            "tahun":"Tahun",
            "f0_":"Jumlah Pengunjung",
            "jenis_wisatawan":"Jenis Wisatawan"
        })
    fig.update_layout(
        hoverlabel=dict(
            bgcolor='white'
        ))
    fig.update_traces(mode="markers+lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("_Sumber : Open Data Jabar_")

# Tren Pendapatan Sektor Wisata Jawa Barat
st.subheader("Tren Pendapatan Sektor Wisata Jawa Barat")

# Dividing Into 2 Columns
col1, col2 = st.columns(2)

with col1:
    fig=px.bar(
        pendapatan_wisata_jabar,
        x="tahun",
        y="jumlah",
        color="sektor_wisata",
        title="Pendapatan Pariwisata Jawa Barat 2014-2020",
        labels={
            "tahun":"Tahun",
            "jumlah":"Jumlah",
            "sektor_wisata":"Sektor Wisata"
        }
    )
    fig.update_layout(
    hoverlabel=dict(
        bgcolor='white'
    ))
    st.plotly_chart(fig, use_container_width=True)
    st.caption("_Sumber : Open Data Jabar_")

with col2:
    st.write("Dapat dilihat dari grafik di samping bahwa tren total pendapatan pariwisata Jawa Baran **_terus mengalami peningkatan tetapi mengalami penurunan tajam pada tahun 2020._** Total pendapatan terbesar dimiliki oleh tahun 2019 dengan komposisi penerimaan tertinggi pada retribusi dan terendan pada hiburan. Sedangkan saat pandemi terjadi yaitu pada tahun 2020, total pendapatan menurun drastis dengan pendapatan restoran/rumah makan sebagai komposisi pendapatan tertinggi dan hiburan sebagai pendapatan terendah.")

# Tren Mobilitas Masyarakat (Menurut Google Mobility Index)
st.subheader("Tren Mobilitas Masyarakat (Menurut Google Mobility Index)")
st.write("_Dataset_ ini menunjukkan perubahan kunjungan dan durasi menetap di berbagai tempat yang dibandingkan dengan dasar pengukuran. Google menghitung perubahan ini menggunakan jenis data yang digabungkan dan dianonimkan, sama seperti jenis data yang digunakan untuk menampilkan jam favorit untuk tempat di Google Maps.")
st.write("Dasar pengukurannya adalah nilai **_median untuk hari yang sesuai selama periode 5 minggu, yaitu 3 Jan-6 Feb 2020._** _Dataset_ menunjukkan tren selama beberapa bulan dan data terbarunya menunjukkan tren selama 2-3 hari terakhir—ini adalah durasi yang diperlukan untuk menghasilkan _dataset_.")
st.write("Jenis data yang disertakan dalam penghitungan bergantung pada setelan pengguna, konektivitas, dan apakah data tersebut mencapai ambang privasi Google atau tidak. Jika data tersebut tidak memenuhi ambang kualitas dan privasi, beberapa tempat dan tanggal mungkin akan terlihat kolom dan _values_ yang kosong.")
st.caption("*Catatan : _Value_ pada setiap kategori tempat difilter menggunakan _savgol_filter_ pada library _scipy_")

# Using Savgol Filter to Smoothens the Line
mobilitas_jabar['Tempat_Rekreasi'] = signal.savgol_filter(mobilitas_jabar['Tempat_Rekreasi'], 15, 1)
mobilitas_jabar['Pusat_Perbelanjaan_dan_Apotek'] = signal.savgol_filter(mobilitas_jabar['Tempat_Rekreasi'], 15, 1)
mobilitas_jabar['Taman'] = signal.savgol_filter(mobilitas_jabar['Tempat_Rekreasi'], 15, 1)
mobilitas_jabar['Stasiun_Transit'] = signal.savgol_filter(mobilitas_jabar['Tempat_Rekreasi'], 15, 1)
mobilitas_jabar['Perkantoran'] = signal.savgol_filter(mobilitas_jabar['Tempat_Rekreasi'], 15, 1)
mobilitas_jabar['Perumahan'] = signal.savgol_filter(mobilitas_jabar['Tempat_Rekreasi'], 15, 1)


CHOICES = {"Tempat_Rekreasi":"Tempat Rekreasi",
           "Pusat_Perbelanjaan_dan_Apotek":"Pusat Perbelanjaan dan Apotek",
           "Taman":"Taman",
           "Stasiun_Transit":"Stasiun Transit",
           "Perkantoran":"Perkantoran",
           "Perumahan":"Perumahan"}

def format_func(option):
    return CHOICES[option]

category_option = st.selectbox("Pilih Kategori",
                               options=list(CHOICES.keys()), format_func=format_func)
fig=px.line(
    mobilitas_jabar,
    x='daily',
    y=category_option,
    title='Indeks Mobilitas Jawa Barat 2020-2022',
    labels={
        "daily":"Tanggal",
        "Tempat_Rekreasi":"Indeks Mobilitas Tempat Rekreasi",
        "Pusat_Perbelanjaan_dan_Apotek":"Indeks Mobilitas Pusat Perbelanjaan dan Apotek",
        "Taman":"Indeks Mobilitas Taman",
        "Stasiun_Transit":"Indeks Mobilitas Stasiun Transit",
        "Perkantoran":"Indeks Mobilitas Perkantoran",
        "Perumahan":"Indeks Mobilitas Perumahan"
    }
)
st.plotly_chart(fig, use_container_width=True)