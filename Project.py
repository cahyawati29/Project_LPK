#library
import streamlit as st

#write
st.title('Software Perhitungan')
st.subheader('Kalkulator Titrimetri')
st.write('Kalkulator ini berguna untuk menghitung Normalitas, Molaritas, Kadar%(b/v), Kadar PPM, Penentuan jenis larutan berdasarkan pH, dan perhitungan pH')
st.divider()

option = st.selectbox(
    'Silahkan pilih',
    ('Normalitas', 'Molaritas', 'Kadar(% b/v)', 'Kadar(PPM)', 'Penentuan jenis larutan berdasarkan pH', 'Perhitungan pH'))


if option=='Normalitas':
    Bobot = st.number_input('Masukkan bobot yang diketahui, dalam satuan mg')
    BE = st.number_input('Masukkan BE sampel, dalam satuan mg/mgrek')
    Vsampel = st.number_input('Masukkan volume sampel, dalam satuan mL')
    FP = st.number_input('Masukkan faktor pengali yang diketahui')
    if st.button('HITUNG'):
        Normalitas = Bobot/(BE*Vsampel*FP)
        st.success(f'Normalitas yang didapat adalah {Normalitas} mgrek/mL')
    
elif option=='Molaritas':
    Bobot = st.number_input('Masukkan bobot yang diketahui, dalam satuan mg')
    BM = st.number_input('Masukkan BM sampel, dalam satuan mg/mmol')
    Vsampel = st.number_input('Masukkan volume sampel, dalam satuan mL')
    FP = st.number_input('Masukkan faktor pengali yang diketahui')
    if st.button('HITUNG'):
        Molaritas = Bobot/(BM*Vsampel*FP)
        st.success(f'Molaritas yang didapat adalah {Molaritas} mmol/mL')
    
elif option=='Kadar(% b/v)':
    BE = st.number_input('Masukkan BE sampel, dalam satuan mg/mgrek')
    N = st.number_input('Masukkan normalitas yang diketahui, dalam satuan mgrek/mL')
    FP = st.number_input('Masukkan faktor pengali yang diketahui')
    Volume_titran = st.number_input('Masukkan volume titran yang diketahui, dalam satuan mL')
    Vsampel = st.number_input('Masukkan volume sampel, dalam satuan mL')
    if st.button('HITUNG'):
        Kadar = Volume_titran*BE*N*FP*100*0.001/Vsampel
        st.success(f'Kadar % b/v yang didapatkan adalah {Kadar} % b/v')
        
elif option=='Kadar(PPM)':
    Volume_titran = st.number_input('Masukkan volume titran yang diketahui, dalam satuan mL')
    BM = st.number_input('Masukkan BM sampel, dalam satuan mg/mmol')
    M = st.number_input('Masukkan molaritas yang diketahui, dalam satuan mmol/mL')
    FP = st.number_input('Masukkan faktor pengali yang diketahui')
    Vsampel = st.number_input('Masukkan volume sampel, dalam satuan L')
    if st.button('HITUNG'):
        Kadar_PPM = Volume_titran*BM*M*FP/Vsampel
        st.success(f'Kadar PPM yang didapatkan adalah {Kadar_PPM} mg/L')
        
elif option=='Penentuan jenis larutan berdasarkan pH':
    #dictionary
    dictPh = {
        'Merah': 'Asam Kuat',
        'Jingga': 'Asam Lemah',
        'Kuning': 'Asam Sangat Lemah',
        'Hijau': 'Netral',
        'Biru': 'Basa Sangat Lemah',
        'Ungu': 'Basa Lemah',
        'Violet': 'Basa Kuat'
    }

    # input dari user
    pH = st.number_input("Masukkan nilai pH nya: ")
    st.write('pH nya adalah ', pH)

    #hasil
    def output():
        if pH < 1 or pH > 14:
            st.write("Nilai Ph tidak valid, silahkan masukkan angka mulai dari 1-14")
        elif pH >= 1 and pH <= 3:
            st.write("Nilai Ph memiliki sifat" + dictPh["Merah"], 'dengan warna Merah')
        elif pH >= 3 and pH <= 5:
            st.write("Nilai Ph memiliki sifat " + dictPh["Jingga"], 'dengan warna Jingga')
        elif pH >= 5 and pH <= 6:
            st.write("Nilai Ph memiliki sifat " + dictPh["Kuning"], 'dengan warna Kuning')
        elif pH >= 6 and pH <= 7:
            st.write("Nilai Ph memiliki sifat " + dictPh["Hijau"], 'dengan warna Hijau')
        elif pH >= 7 and pH <= 8:
            st.write("Nilai Ph memiliki sifat " + dictPh["Biru"], 'dengan warna Biru')
        elif pH >= 8 and pH <= 10:
            st.write("Nilai Ph memiliki sifat " + dictPh["Ungu"], 'dengan warna Ungu')
        elif pH >= 10 and pH <= 14:
            st.write("Nilai Ph memiliki sifat " + dictPh["Violet"], 'dengan warna Violet')

    #output
    output()


elif option=='Perhitungan pH':
    option = st.selectbox(
        'Pilih:',
        ('Asam Kuat dengan basa kuat', 'Asam Lemah dengan basa kuat', 'Basa lemah dengan asam kuat', 'Basa kuat dengan asam kuat'))
    if option=='Asam Kuat dengan basa kuat':
        mmol = st.number_input('Masukkan jumlah mmol asam yang diketahui, dalam satuan mmol')
        st.write(f'Nilai mmol adalah {mmol} mmol')
        v = st.number_input('Masukkan volume total larutan yang diketahui, dalam satuan mL')
        st.write(f'Nilai volume adalah {v} mL')
        if st.button('HITUNG'):
            H = mmol/v
            import numpy as np
            pH = -1*np.log10(H)
            st.success(f'pH yang didapatkan adalah {pH}')
    if option=='Asam Lemah dengan basa kuat':
        mmol = st.number_input('Masukkan mmol yang diketahui')
        st.write(f'Nilai mmol adalah {mmol} mmol')
        v = st.number_input('Masukkan volume total larutan yang diketahui, dalam satuan mL')
        st.write(f'Nilai volume adalah {v} mL')
        if st.button('HITUNG'):
            OH=mmol/v
            import numpy as np
            pOH = -1*np.log10(OH)
            pH = 14-(pOH)
            st.success(f'pH yang didapatkan adalah {pH}')  
    if option=='Basa lemah dengan asam kuat':
        mmol = st.number_input('Masukkan jumlah mmol asam yang diketahui, dalam satuan mmol')
        st.write(f'Nilai mmol adalah {mmol} mmol')
        v = st.number_input('Masukkan volume total larutan yang diketahui, dalam satuan mL')
        st.write(f'Nilai volume adalah {v} mL')
        if st.button('HITUNG'):
            H=mmol/v
            import numpy as np
            pH=-1*np.log10(H)
            st.success(f'pH yang didapatkan adalah {pH}')
    if option=='Basa kuat dengan asam kuat':
        mmol = st.number_input('Masukkan jumlah mmol asam yang diketahui, dalam satuan mmol')
        st.write(f'Nilai mmol adalah {mmol} mmol')
        v = st.number_input('Masukkan volume total larutan yang diketahui, dalam satuan mL')
        st.write(f'Nilai volume adalah {v} mL')
        if st.button('HITUNG'):
            H=mmol/v
            import numpy as np
            pOH=-1*np.log10(H)
            pH=-1*np.log10(H)
            st.success(f'pH yang didapatkan adalah {pH}')
                

st.divider()
st.header('Kelompok 11')
st.write('Oleh kelompok 11:')
st.write('Agmy Permata Muchtar (2219027)')
st.write('Cahyawati Ameiliyani Putri (2219049)')
st.write('Cantika Deslia Safitri (2219050)')
st.write('Maia Maharani Nasita Wibowo (2219103)')
st.write('Zulthia Kusumawathy (2219189)')
