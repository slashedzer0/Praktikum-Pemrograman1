# untuk memberi efek warna dan format teks pada output
from rich.console import Console
from rich.table import Table 
console = Console()

import pyfiglet
import platform
import os

def main():
    # untuk membersihkan output
    def clearScreen():
        if (platform.system().lower() == "windows"):
            cmdtorun = 'cls'

        else:
            cmdtorun = 'clear'   
        os.system(cmdtorun)

    # untuk mengulang permainan
    def retry():
        console.print("[b gold1]<Q>[/] [gold1]Kembali ke Menu Utama?[/] (y/n)")
        retry = console.input("[b sea_green3]<A>[/] ").lower()

        if retry.startswith('y'):
            clearScreen()
            main()
        
        elif retry.startswith('n'):
            print()
            exit()

        else:
            print()
            console.print("[b sky_blue2]<I>[/] [sky_blue2]Input tidak valid!")
            print()
            exit()
            
    # untuk memberi petunjuk sebelum memulai cerita
    def hint():
        console.print("[b sky_blue2]<I>[/] Tekan [u b bright_cyan]ENTER[/] untuk melanjutkan cerita. [u b red1]CTRL+C[/] untuk batal.")
        input()
    
    # judul cerita dalam bentuk ascii text
    title1 = pyfiglet.figlet_format("Man  v  The Forest")
    title2 = pyfiglet.figlet_format("Unemployed Reincarnated")

    # MAIN STORY 1 -- bagian Doni
    def story1():
        def story1_subMain():
            def altEnding():
                print("...")
                input()
                print("Dengan bertaruh antara hidup atau mati, pada akhirnya kamu membalas suara teriakan tersebut.")
                input()
                print("Setelah kamu membalas, suara teriakan itu terdiam dan tidak merespon.")
                input()
                print("Tiba-tiba dari arah belakang...")
                input()
                print("Kamu mendengar teriakan seseorang meminta tolong.")
                input()
                print("Kamu pun berlari menuju sumber suara teriakan itu.")
                input()
                print("Rupanya itu adalah salah satu teman rombonganmu yang kakinya terkilir.")
                input()
                print("Kamu bergegas untuk menolong, tetapi sebelum kamu sampai untuk menolong...")
                input()
                print("Kamu melihat semua rombonganmu yang kamu kenal berlari ke sana mendahuluimu.")
                input()
                print("Lalu kamu menyadari ada yang janggal.")
                input()
                print("Semua temanmu tidak melihat ke arahmu, atau bahkan mendengar kamu berbicara, mereka mengabaikan keberadaanmu.")
                input()
                print("Ketika kamu berjalan mendekati mereka, kamu mendengar seseorang teman berbicara mengenai dirimu.")
                input()
                print("Apa yang dikatakannya adalah...")
                input()
                clearScreen()
                console.print('[i bright_white]"Orang itu sudah dinyatakan meninggal 3 hari yang lalu, mengapa kita kembali seolah-olah dia ada di sini?"')
                input()

                console.print("[b bright_white on sky_blue2]  THE END  ")
                print()
                retry()

            def trueEnding():
                print("...")
                input()
                print("Setelah kamu tersadar, kamu sudah berada di rumah sakit.")
                input()
                print("Di ruangan itu tidak ada siapa pun, hanya terdengar suara EKG yang mengukur kecepatan detak jantungmu...")
                input()
                print("Kamu memperhatikan ruangan dan menemukan sebuah surat.")
                input()
                print("Isi dari surat itu adalah...")
                input()
                clearScreen()
                console.print('[i bright_white]"Terima kasih telah bermain Text-Based Adventure."')
                input()

                console.print("[b bright_white on sky_blue2]  THE END  ")
                print()
                retry()

            def subMain_2():
                print("...")
                input()
                print("Rupanya, semua yang baru kamu alami tadi adalah mimpi.")
                input()
                print("Kamu mengalami kebingungan karena kamu tidak ingat di mana terakhir kali kamu tertidur.")
                input()
                print("Lalu kamu berpikir untuk berpindah tempat karena kamu merasa tidak nyaman.")
                input()
                print("Setelah memperhatikan area sekitar, kamu melihat ada jalan yang bercabang...")
                input()
                clearScreen()
                
                console.print("[b gold1]<Q>[/] [gold1]Jalan mana yang kamu ambil?")
                console.print(" a. Jalan lurus (penuh pepohonan tinggi)")
                console.print(" b. Jalan menuju sungai (suhu lebih dingin)")
                answer = console.input("[b sea_green3]<A>[/] ").lower()   

                while answer != '':
                    if answer == 'a':
                        clearScreen()   
                        print("Kamu memutuskan untuk mengikuti jalan lurus yang dipenuhi pepohonan tinggi.")
                        input()
                        print("Hingga pada akhirnya kamu tersesat dan terjebak dikelilingi pepohonan tinggi yang gelap...")
                        input()
                        print("Kamu pun hampir putus asa dan mulai stres.")
                        input()
                        print("Tiba-tiba saja...")
                        input()
                        print("Ada suara teriakan manusia yang memanggil namamu dari jauh.")
                        input()
                        print("Sebaliknya, kamu tidak cukup yakin yang memanggil itu adalah rombonganmu.")
                        input()
                        print("Kamu dibuat cemas oleh dirimu sendiri dan bimbang apakah kamu sedang berhalusinasi atau tidak.")
                        input()
                        print("Di samping itu, suara teriakan itu semakin menjauh dan semakin hilang...")
                        input()
                        clearScreen()

                        console.print("[b gold1]<Q>[/] [gold1]Apakah kamu ingin membalas suara teriakan itu?[/] (y/n)")
                        answer = console.input("[b sea_green3]<A>[/] ").lower()

                        while answer != '':
                            if answer.startswith('y'):
                                clearScreen()
                                altEnding()
                                break

                            elif answer.startswith('n'):
                                clearScreen()
                                print("Karena kamu tidak yakin dengan sumber suara tersebut, kamu memutuskan untuk diam.")
                                input()
                                print("Lalu suara itu pun menghilang tanpa jejak...")
                                input()
                                print("Malang sekali bagimu, ternyata itu adalah rombongan yang mencari keberadaanmu.")
                                input()
                                print("Kamu membuang kesempatan terbaikmu untuk kembali.")
                                input()
                                clearScreen()

                                console.print("[b bright_white on red1]  GAME OVER  ")
                                print()
                                retry()
                                break

                            else:
                                print()
                                console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan y/n.")
                                answer = console.input("[b sea_green3]<A>[/] ").lower()

                    elif answer == 'b':
                        clearScreen()
                        print("Pada akhirnya kamu mengikuti sungai.")
                        input()
                        print("Berharap menemui penduduk sekitar yang tinggal di dekat sungai...")
                        input()
                        print("Di tengah perjalananmu, salah satu kakimu tanpa sengaja tergigit ular berbisa.")
                        input()
                        print("Kamu mengalami shock akibat gigitan ular itu.")
                        input()
                        clearScreen()

                        console.print("[b gold1]<Q>[/] [gold1]Apa yang seharusnya kamu lakukan?")
                        console.print(" a. Hisap luka dengan mulut")
                        console.print(" b. Ikat luka dengan kain")
                        console.print(" c. Tetap diam dan tidak banyak gerak")
                        answer = console.input("[b sea_green3]<A>[/] ").lower()

                        while answer != '':
                            if answer == 'a':
                                clearScreen()
                                print("Dengan refleks, kamu menghisap luka tersebut.")
                                input()
                                print("Usai menghisap tubuhmu keracunan oleh bisa ular...")
                                input()
                                print("Kamu mati konyol akibat kurang edukasi.")
                                input()
                                clearScreen()

                                console.print("[b bright_white on red1]  GAME OVER  ")
                                print()
                                retry()
                                break

                            elif answer == 'b':
                                clearScreen()
                                print("Kamu mulai panik dan merobek bajumu untuk mengikat luka itu.")
                                input()
                                print("Namun setelah itu...")
                                input()
                                print("Kamu mengalami rasa sakit yang hebat di bagian luka tersebut.")
                                input()
                                print("Ternyata rasa sakit itu bersumber dari robekan bajumu yang tidak steril dan dipenuhi bakteri.")
                                input()
                                print("Badanmu mulai pucat dan lemas.")
                                input()
                                print("Kamu tewas karena tidak sanggup menahan luka yang semakin parah.")
                                input()
                                clearScreen()

                                console.print("[b bright_white on red1]  GAME OVER  ")
                                print()
                                retry()
                                break

                            elif answer == 'c':
                                clearScreen()
                                print("Kamu tetap diam dan mengurangi gerakan yang tidak perlu untuk memperlambat racun menyebar.")
                                input()
                                print("Setelah cukup lama menunggu, ada seseorang yang menyadari keberadaanmu.")
                                input()
                                print("Orang itu berlari mendekat dan menuju ke tempatmu.")
                                input()
                                print("Kamu mencoba untuk bangkit tetapi badanmu mulai melemah dan pada akhirnya pingsan...")
                                input()
                                clearScreen()
                                trueEnding()
                                break

                            else:
                                print()
                                console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan a/b/c.")
                                answer = console.input("[b sea_green3]<A>[/] ").lower()
                    
                    else:
                        print()
                        console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan a/b.")
                        answer = console.input("[b sea_green3]<A>[/] ").lower()

            def subMain_1():
                print("...")
                input()
                print("Di tengah malam, kamu terbangun akibat mendengar suara aneh.")
                input()
                print("Kamu memutuskan untuk bergegas pergi dari tempatmu.")
                input()
                print("Dalam perjalananmu, kamu menemukan sebuah bangunan tua peninggalan Perang Dunia II yang terbengkalai...")
                input()
                print("Kamu penasaran untuk pergi masuk ke dalam bangunan itu.")
                input()
                clearScreen()
                
                console.print("[b gold1]<Q>[/] [gold1]Terdapat 3 jalur masuk, jalur mana yang kamu pilih?")
                console.print(" a. Jalur A (gelap, bau menyengat)")
                console.print(" b. Jalur B (sedikit terang, sempit)")
                console.print(" c. Jalur C (gelap, penuh kabel listrik)")
                answer = console.input("[b sea_green3]<A>[/] ").lower()

                while answer != '':
                    if answer == 'a':
                        clearScreen()
                        print("Dengan ragu-ragu, kamu masuk jalur ini dan berharap tidak terjadi apa-apa.")
                        input()
                        print("Rupanya di jalur masuk ini, terdapat banyak jenis ular yang menghalangi jalan.")
                        input()
                        print("Kamu mencoba kembali keluar tetapi kamu sudah dihadang oleh kawanan ular yang lain.")
                        input()
                        print("Kamu tewas mengenaskan.")
                        input()
                        clearScreen()

                        console.print("[b bright_white on red1]  GAME OVER  ")
                        print()
                        retry()
                        break

                    elif answer == 'b':
                        clearScreen()
                        print("Dengan tergesa-gesa, kamu masuk melalui jalur kedua.")
                        input()
                        print("Tapi...")
                        input()
                        print("Saat kamu berjalan cukup jauh ke dalam, kamu terkena jebakan mematikan yang masih aktif.")
                        input()
                        print("Kamu gagal dan tewas secara mengenaskan.")
                        input()
                        clearScreen()

                        console.print("[b bright_white on red1]  GAME OVER  ")
                        print()
                        retry()
                        break

                    elif answer == 'c':
                        clearScreen()
                        print("Kamu sadar tidak ada arus listrik aktif di tengah hutan.")
                        input()
                        print("Dengan waspada, kamu mulai berjalan masuk...")
                        input()
                        print("Setelah berhasil masuk, kamu menjumpai 3 pintu masuk lagi.")
                        input()
                        print("Masing-masing dari pintu itu terdapat gambar hewan hibrida.")
                        input()
                        clearScreen()

                        console.print("[b gold1]<Q>[/] [gold1]Pintu mana yang kamu pilih?")
                        console.print(" a. Pintu A (gambar kepala badak berbadan lebah)")
                        console.print(" b. Pintu B (gambar kepala kelinci berbadan buaya)")
                        console.print(" c. Pintu C (gambar kepala babi berbadan trenggiling)")
                        answer = console.input("[b sea_green3]<A>[/] ").lower()
                        
                        while answer != '':
                            if answer == 'a':
                                clearScreen()
                                print("Kamu memutuskan untuk melawan hewan hibrida kepala badak berbadan lebah.")
                                input()
                                print("Walaupun terlihat beringas, untuk suatu alasan hewan hibrida itu langsung mati dengan sendirinya.")
                                input()
                                print("Hewan hibrida itu mati akibat tidak dapat menopang kepala yang bebannya lebih besar daripada badannya.")
                                input()
                                print("Setelah menang, tiba-tiba ada cahaya yang sangat terang menghampirimu...")
                                input()
                                clearScreen()
                                subMain_2()
                                break

                            elif answer == 'b':
                                clearScreen()
                                print("Kamu memutuskan untuk melawan hewan hibrida kepala kelinci berbadan buaya.")
                                input()
                                print("Ternyata, kepala kelinci itu berevolusi menjadi kepala buaya...")
                                input()
                                print("Hewan hibrida itu menerkammu hingga kamu terluka sangat parah.")
                                input()
                                print("Kamu tidak bisa menahan luka dan tewas.")
                                input()
                                clearScreen()
                                    
                                console.print("[b bright_white on red1]  GAME OVER  ")
                                print()
                                retry()
                                break

                            elif answer == 'c':
                                clearScreen()
                                print("Kamu memutuskan untuk melawan hewan hibrida kepala babi berbadan trenggiling.")
                                input()
                                print("Alih-alih menjadi jinak, hewan hibrida itu berevolusi menjadi monster mengerikan yang tidak pernah kamu bayangkan...")
                                input()
                                print("Kamu mengalami shock berat dan tidak dapat menggerakan seluruh badanmu.")
                                input()
                                print("Hingga akhirnya kamu terkena serangan jantung dan mati.")
                                input()
                                clearScreen()
                                    
                                console.print("[b bright_white on red1]  GAME OVER  ")
                                print()
                                retry()
                                break

                            else:
                                print()
                                console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan a/b/c.")
                                answer = console.input("[b sea_green3]<A>[/] ").lower()

                    else:
                        print()
                        console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan a/b/c.")
                        answer = console.input("[b sea_green3]<A>[/] ").lower()

            print("...")
            input()
            print("Setelah melewati malam yang panjang, kamu terbangun dan mulai kehausan.")
            input()
            print("Akhirnya kamu memutuskan untuk mencari sumber air yang ada di sekitar.")
            input()
            print("Beruntung bagimu, kamu menemukan 3 sumber air ada di depan matamu.")
            input()
            clearScreen()
                                        
            console.print("[b gold1]<Q>[/] [gold1]Sumber air mana yang akan kamu minum?")
            console.print(" a. Sungai deras")
            console.print(" b. Pohon anggur dan tanaman")
            console.print(" c. Tidak yakin dan batal minum")
            answer = console.input("[b sea_green3]<A>[/] ").lower()
            
            while answer != '':
                if answer == 'a':
                    clearScreen()
                    print("Setelah mempertimbangkan semua, kamu memilih meminum air sungai.")
                    input()
                    print("Kamu berpikir bahwa air sungai terus mengalir sehingga meminimalisir terkena penyakit.")
                    input()
                    print("Setelah merasa segar, kamu melanjutkan perjalanan untuk mencari rombonganmu.")
                    input()
                    print("Tetapi hingga waktu malam, kamu tidak menemukan jejak mereka.")
                    input()
                    print("Udara mulai terasa dingin dan keadaan memaksamu untuk membuat api unggun.")
                    input()
                    print("Setelah beberapa saat mencari bahan untuk dibakar, kamu berhasil membuat api.")
                    input()
                    print("Tepat setelah itu, kamu merasa lapar dan harus mencari sesuatu untuk dimakan.")
                    input()
                    print("Setelah mencari ke sana kemari, kamu menemukan beberapa bahan makanan.")
                    input()
                    clearScreen()

                    console.print("[b gold1]<Q>[/] [gold1]Mana yang akan kamu makan?")
                    console.print(" a. Berry merah/ungu")
                    console.print(" b. Batang pohon pinus")
                    console.print(" c. Jamur")
                    answer = console.input("[b sea_green3]<A>[/] ").lower()

                    while answer != '':
                        if answer == 'a':
                            clearScreen()
                            print("Kamu memutuskan untuk memakan berry yang terlihat segar.")
                            input()
                            print("Berry itu mengandung racun.")
                            input()
                            print("Kamu tewas dalam waktu singkat.")
                            input()
                            clearScreen()

                            console.print("[b bright_white on red1]  GAME OVER  ")
                            print()
                            retry()
                            break

                        elif answer == 'b':
                            clearScreen()
                            print("Batang pohon pinus adalah opsi yang paling aman.")
                            input()
                            print("Kamu memasaknya dengan api unggun yang kamu buat.")
                            input()
                            print("Selesai makan, tanpa sadar kamu pun mulai tertidur karena kelelahan.")
                            input()
                            clearScreen()
                            subMain_1()
                            break

                        elif answer == 'c':
                            clearScreen()
                            print("Dengan keterbatasan pengetahuanmu, kamu nekat untuk memakan jamur liar.")
                            input()
                            print("Tubuhmu merespon dengan buruk...")
                            input()
                            print("Kamu tewas keracunan.")
                            input()
                            clearScreen()

                            console.print("[b bright_white on red1]  GAME OVER  ")
                            print()
                            retry()
                            break
                        
                        else:
                            print()
                            console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan a/b/c.")
                            answer = console.input("[b sea_green3]<A>[/] ").lower()

                elif answer == 'b':
                    clearScreen()
                    print("Kamu tergoda oleh pohon anggur yang terlihat segar.")
                    input()
                    print("Kemudian memetik buah itu dan memakannya...")
                    input()
                    print("Tidak butuh waktu lama, tubuhmu terkena racun mematikan.")
                    input()
                    print("Kamu tewas keracunan.")
                    input()
                    clearScreen()
                    
                    console.print("[b bright_white on red1]  GAME OVER  ")
                    print()
                    retry()
                    break

                elif answer == 'c':
                    clearScreen()
                    print("Dengan berat hati, kamu menahan hausmu karena tidak yakin dengan kualitas air yang ada.")
                    input()
                    print("Lalu pergi dan segera melanjutkan pencarian rombonganmu.")
                    input()
                    print("Namun...")
                    input()
                    print("Seperti yang diduga, tubuhmu mulai melemah dan mengalami dehidrasi hebat.")
                    input()
                    print("Kamu mati konyol akibat melewatkan kesempatan emas.")
                    input()
                    clearScreen()

                    console.print("[b bright_white on red1]  GAME OVER  ")
                    print()
                    retry()
                    break
                
                else:
                    print()
                    console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan a/b/c.")
                    answer = console.input("[b sea_green3]<A>[/] ").lower()

        # cerita dimulai dari sini
        print("...")
        input()
        print("Kamu dan teman-temanmu sedang melakukan camping di sebuah gunung.")
        input()
        print("Singkat cerita, kamu terpisah dari rombongan...")
        input()
        print("Di tengah perjalanan saat mencari rombonganmu, tiba-tiba kamu menemukan seekor anak beruang liar.")
        input()
        clearScreen()
            
        console.print("[b gold1]<Q>[/] [gold1]Apa yang akan kamu lakukan?")
        console.print(" a. Main dengan anak beruang")
        console.print(" b. Pergi menjauh secara perlahan")
        answer = console.input("[b sea_green3]<A>[/] ").lower()

        while answer != '':
            if answer == 'a':
                clearScreen()
                print("Tentu saja! Bermain dengan anak beruang adalah kesempatan langka.")
                input()
                print("Tapi...")
                input()
                print("Tidak lama setelah itu, induk beruang muncul dan menyergapmu dengan ganas hingga kamu kehabisan darah.")
                input()
                print("Kamu tewas di tempat.")
                input()
                clearScreen()

                console.print("[b bright_white on red1]  GAME OVER  ")
                print()
                retry()
                break

            elif answer == 'b':
                clearScreen()
                print("Dengan waspada, kamu segera menjauh dan menyadari kemungkinan adanya induk dari anak beruang itu yang siap menyerangmu secara brutal.")
                input()
                print("Setelah berlari cukup jauh, kamu memutuskan untuk beristirahat sebentar.")
                input()
                print("Namun tiba-tiba...")
                input()
                print("Kamu mendengar suara ranting pohon patah yang sumbernya cukup dekat.")
                input()
                print("Kemudian, setelah mengintip sedikit, ternyata itu adalah seekor induk beruang yang kelaparan.")
                input()
                print("Beruang itu menyadari keberadaanmu dan berlari mengejarmu.")
                input()
                clearScreen()

                console.print("[b gold1]<Q>[/] [gold1]Ke mana kamu akan pergi?")
                console.print(" a. Berlari sejauh mungkin")
                console.print(" b. Memanjat pohon")
                console.print(" c. Terjun ke kubang lumpur")
                answer = console.input("[b sea_green3]<A>[/] ").lower()
                
                while answer != '':
                    if answer == 'a':
                        clearScreen()
                        print("Tanpa pikir panjang, kamu berlari dengan sekuat tenaga.")
                        input()
                        print("Kamu tertangkap dan berakhir dengan tragis.")
                        input()
                        clearScreen()

                        console.print("[b bright_white on red1]  GAME OVER  ")
                        print()
                        retry() 
                        break     

                    elif answer == 'b':
                        clearScreen()
                        print("Kamu memanjat pohon terdekat dan berharap beruang itu pergi meninggalkanmu.")
                        input()
                        print("Nahas, beruang yang kelaparan itu ternyata bisa memanjat pohon dan menghabisimu.")
                        input()
                        clearScreen()

                        console.print("[b bright_white on red1]  GAME OVER  ")
                        print()
                        retry() 
                        break 

                    elif answer == 'c':
                        clearScreen()
                        print("Dengan cepat, kamu terjun ke kubang lumpur dan melumuri badanmu untuk menghilangkan bau.")
                        input()
                        print("Beruang itu tidak dapat mencium baumu dan tidak lama kemudan pergi meninggalkanmu.")
                        input()
                        print("Bersamaan dengan itu, kamu pun mulai kelelahan dan pingsan...")
                        input()
                        clearScreen()
                        story1_subMain()
                        break   

                    else:
                        print()
                        console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan a/b/c.")
                        answer = console.input("[b sea_green3]<A>[/] ").lower()

            else:
                print()
                console.print("[b sky_blue2]<I>[/] [sky_blue2]Mohon jawab dengan pilihan a/b.")
                answer = console.input("[b sea_green3]<A>[/] ").lower()
                
    # STORY 2 -- bagian Angga
    def story2():
        print("...")
        input()
        print("Di suatu masa, hiduplah seorang penggemar 2 dimensi, pengangguran dan jomblo.")
        input()
        print("Ia hidup di dunia tipu-tipu dan terjebak hutang yang melilitnya.")
        input()
        print("Suatu malam ia keluar untuk membeli rokok di minimarket, namun saat membayar perutnya merasa kesakitan.")
        input()
        print("Rupanya dia sudah menahannya sejak seminggu yang lalu.")
        input()
        print("Dia masih tetap memaksa untuk menahan kesakitan tersebut.")
        input()
        clearScreen()

        console.print("[b gold1]<Q>[/] [gold1]Buang air di rumah?[/] (y/n)")
        answer = console.input("[b sea_green3]<A>[/] ").lower()
        if answer == 'y':
            clearScreen()
            print("Kemudian ia berlari sekencang mungkin untuk pulang, tapi di perjalanan ia tidak sengaja menginjak kulit pisang dan jatuh terbanting.")
            input()
            print("“Apa apaan, apa aku akan mati karena menahan berak?” dengan hembusan pasrah.")
            input()
            print("Tiba-tiba ia terbangun di sebuah kandang kambing yang penuh bau kotoran...")
            input()
            print("Ternyata itu bukan bau kotoran namun bau badannya sendiri yang belum mandi selama 2 minggu.")
            input()
            clearScreen()
            print("...")
            input()
            print("Dia bereinkarnasi ke dunia lain sebagai seorang petualang, dia mulai mencari uang di dunia itu dari mengemis hingga menjadi kuli bangunan.")
            input()
            print("Beberapa minggu ia sudah dapat mengumpulkan uang dan ia berencana untuk membeli sebuah pedang di pasar gelap.")
            input()
            print("Sesampainya di sana dia dihadapkan dengan 2 pedang yang sangat misterius dan pedang yang sangat langka.")
            input()
            clearScreen()

            console.print("[b gold1]<Q>[/] [gold1]Beli pedang misterius?[/] (y/n)")
            answer = console.input("[b sea_green3]<A>[/] ").lower()
            if answer == 'y':
                clearScreen()
                print("“Pedang ini sangat cocok untuk seorang pengangguran sepertimu.” kata si penjual.")
                input()
                print("Ia pun membeli pedang itu, tak disangka ia langsung mendapatkan sebuah skill misterius.")
                input()
                print("Kemudian ia langsung pergi berpetualang untuk meningkatkan skill karena yang ia miliki hanya skill seorang kuli Jawa.")
                input()
                clearScreen()

                console.print("[b gold1]<Q>[/] [gold1]Pergi ke hutan untuk berpetualang?[/] (y/n)")
                answer = console.input("[b sea_green3]<A>[/] ").lower()
                if answer == 'y':
                    clearScreen()
                    print("Ia mulai menjelajahi hutan dan ia merasa lapar, namun ia lupa membawa bekal.")
                    input()
                    print("Dia mencoba mencari buruan untuk dapat dimakan di hutan itu.")
                    input()
                    print("Saat di perjalanan ia tidak sengaja bertemu monster hutan tersebut, yaitu seekor monster babi hutan.")
                    input()
                    print("Dia mencoba melawan monster tersebut untuk dijadikan santapannya.")
                    input()
                    print("Tak disangka monster tersebut menyerang lebih awal, ia terhempas jauh ke belakang, dia kesakitan dan tak bisa bangun.")
                    input()
                    clearScreen()
                    print("“Hai orang pengangguran, apa kau akan mati dengan cara konyol seperti ini?” kata si pedang.")
                    input()
                    print("Dia kebingungan asal suara tersebut.")
                    input()
                    print("“Aku di sini bodoh, aku akan menawarkan bantuan padamu jika kau tak ingin mati, bagaimana?” tanya si pedang.")
                    input()
                    clearScreen()

                    console.print("[b gold1]<Q>[/] [gold1]Terima bantuan?[/] (y/n)")
                    answer = console.input("[b sea_green3]<A>[/] ").lower()
                    if answer == 'y':
                        clearScreen()
                        print("“Baiklah bodoh, pegang aku erat-erat!” kata si pedang.")
                        input()
                        print("Ia langsung terhempas bersama pedang itu setelah menyerang si monster.")
                        input()
                        print("Dengan sekali kekuatan misterius si pedang, babi hutan tersebut langsung tewas.")
                        input()
                        print("“Tch, cuma begini? Apa kau tidak bisa melawannya? Apa skill yang kau miliki hanya berkuli?” tanya si pedang.")
                        input()
                        print("Ia hanya diam kebingungan terhadap pedangnya sendiri.")
                        input()
                        print("Pedang itu langsung menyerap jiwa monster babi hutan itu sebagai makanannya.")
                        input()
                        print("Karena ia sangat kelaparan, dia langsung menghampiri mayat monster babi hutan tadi.")
                        input()
                        clearScreen()

                        console.print("[b gold1]<Q>[/] [gold1]Makan babi hutan sekarang?[/] (y/n)")
                        answer = console.input("[b sea_green3]<A>[/] ").lower()
                        if answer == 'y':
                            clearScreen()
                            print("Karena sudah tidak bisa menahan lapar, ia langsung membakar mayat monster tersebut.")
                            input()
                            print("Tak disangka, ternyata monster itu memiliki kekuatan mengeluarkan racun dari tubuhnya yang sudah mati.")
                            input()
                            print("Ia pun merasa kesakitan.")
                            input()
                            print("Tak perlu waktu lama, ia mati dengan sekejap mata.")
                            input()
                            print("“Bodoh, kau mati oleh makhluk yang sudah mati!” kata si pedang.")
                            input()
                            clearScreen()

                            console.print("[b bright_white on red1]  GAME OVER LOL  ")
                            print()
                            retry()
                        elif answer == 'n':
                            clearScreen()
                            print("Kemudian dia membawa mayat monster tersebut dengan kekuatan kuli jawanya untuk dibawa ke guild para petualang di pusat kota.")
                            input()
                            print("“Siapa kau sebenarnya pedang?” tanya dia.")
                            input()
                            print("“Ha? Kau ingin tau siapa aku? Kau belum cukup kuat untuk mengenalku!” dengan tertawa jahat.")
                            input()
                            clearScreen()
                            
                            print("...")
                            input()
                            print("Ia pun sampai di guild para petualang, baru pertama kali ia ke sana.")
                            input()
                            print("Di sana dia menjual hasil buruannya dan meminta pelayan untuk menjadikan olahan yang enak.")
                            input()
                            clearScreen()
                            
                            console.print("[b gold1]<Q>[/] [gold1]Mau santapan spesial?[/] (y/n)")
                            answer = console.input("[b sea_green3]<A>[/] ").lower()
                            if answer == 'y':
                                clearScreen()
                                print("Kemudian datang pelayan yang sangat cantik jelita, wanita itu mirip dengan wanita yang ia cintai di kehidupan sebelumnya.")
                                input()
                                print("Namun kisah cinta seorang pengangguran seperti dia tidak akan pernah terjadi, dia ditinggal kawin oleh wanita yang pernah ia cintai.")
                                input()
                                print("“Wow, buruan yang hebat tuan, siapa anda sebenarnya?” tanya pelayan.")
                                input()
                                print("Pelayan itu terheran-heran karena buruan yang ia bawa merupakan monster yang sangat sulit dikalahkan.")
                                input()
                                print("Dengan lembut pelayan itu menawarkan olahan spesial dan membeli buruan tersebut dengan jumlah uang yang besar.")
                                input()
                                print("Sebagai bonus dia ditawarkan menjadi anggota guild tersebut dan ia dapat memilih satu dari dua skill yang ditawarkan.")
                                input()
                                clearScreen()

                                console.print("[b gold1]<Q>[/] [gold1]Pilih skill?[/] (1/2)")
                                answer = console.input("[b sea_green3]<A>[/] ").lower()
                                if answer == '1':
                                    clearScreen()
                                    print("Ia mendapatkan skill yang sangat berbahaya yaitu menghancurkan setengah dunia dengan satu mantra.")
                                    input()
                                    print("Dia pun dijauhi oleh para petualangan lain dan pelayan wanita itu dan dikucilkan oleh rakyat.")
                                    input()
                                    print("Kemudian ia dipaksa keluar dari kota tersebut dan menjadi gelandangan.")
                                    input()
                                    clearScreen()

                                    console.print("[b bright_white on red1]  GAME OVER NTNTNT  ")
                                    print()
                                    retry()
                                elif answer == '2':
                                    clearScreen()
                                    print("“Selamat tuan, skill yang anda dapatkan adalah kecerdasan yang melebihi manusia, aku cukup terkesan padamu, tuan!” kata pelayan cantik.")
                                    input()
                                    print("Wanita itu sangat tertarik dengan dia, tak disangka wanita itu juga seorang petualang sama seperti dia.")
                                    input()
                                    print("Dia memiliki magic skill yang luar biasa namun kecerdasannya di bawah rata-rata.")
                                    input()
                                    print("“Bolehkah aku tau namamu?” tanya pelayan cantik itu.")
                                    input()
                                    print("“Bagus! Ini kesempatan bagi seorang jomblo dan pengangguran sepertimu!” jawab si pedang.")
                                    input()
                                    print("“Pedangmu bisa bicara, tuan? Wah hebat sekali!” kata pelayan cantik.")
                                    input()
                                    clearScreen()

                                    console.print("[b gold1]<Q>[/] [gold1]Berkenalan dengan pelayan cantik?[/] (y/n)")
                                    answer = console.input("[b sea_green3]<A>[/] ").lower()
                                    if answer == 'y':
                                        clearScreen()
                                        print("“Salam kenal tuan, namaku adalah Sena!” kata pelayan.")
                                        input()
                                        print("Dengan malu-malu dia mulai memperkenalkan diri kepada pelayan cantik itu.")
                                        input()
                                        print("“Apa kau se-jones itu hingga kau gugup bicara dengan wanita?” si pedang tertawa.")
                                        input()
                                        print("“Aku… Al, salam kenal juga Sena!” jawab dia.")
                                        input()
                                        print("“Apa aku bisa masuk ke kelompok petualangmu, Al?” tanya Sena.")
                                        input()
                                        print("Karena Al juga belum memiliki kelompok ia pun menerima permintaan Sena dan mulai berteman baik dengan dia.")
                                        input()
                                        clearScreen()
                                        print("“Kalau boleh tahu siapa nama pedangmu Al?” tanya Sena.")
                                        input()
                                        print("“Perkenalkan aku adalah reinkarnasi dari seorang ahli pedang, namaku adalah Sa--”")
                                        input()
                                        print("“Tidak, aku belum memberi namamu pedang sialan, namamu adalah Wakuwaku.” Jawab Al.")
                                        input()
                                        print("“Haaa? Aku tidak ingin nama konyol itu!” tanya si pedang dengan kesal.")
                                        input()
                                        print("“Apa itu artinya? Maksudmu bergairah haaa?” Al membalas.")
                                        input()
                                        print("Mereka bertiga pun tertawa bersama dan mulailah kisah baru dari dua orang petualang dan pedangnya yang sangat misterius.")
                                        input()
                                        clearScreen()

                                        console.print("[b bright_white on sky_blue2]  THE END ~ GGWP  ")
                                        print()
                                        retry()
                                    elif answer == 'n':
                                        clearScreen()
                                        print("Sangat disayangkan pelayan itu sangat marah dan benci kepadanya.")
                                        input()
                                        print("Kemudian dia juga dibenci satu guild karena telah menyakiti hati wanita paling cantik yang merupakan kembang desa.")
                                        input()
                                        print("Kehidupan yang ia idam-idamkan yaitu membentuk sebuah harem pun tidak tercipta karena semua wanita menjauhinya.")
                                        input()
                                        clearScreen()

                                        console.print("[b bright_white on sky_blue2]  THE END ~ MENGSEDIH  ")
                                        print()
                                        retry()
                                    else:
                                        exit()
                                else:
                                    exit()
                                    
                            elif answer == 'n':
                                clearScreen()
                                print("Datang seorang pelayan laki-laki yang mempunyai sifat aneh, dia penyuka sesama jenis.")
                                input()
                                print("Dia suka menggoda petualang pemula seperti main character kita ini...")
                                input()
                                print("Kehidupan indah yang dibayangkan tidak akan pernah terjadi.")
                                input()
                                clearScreen()

                                console.print("[b bright_white on red1]  GAME OVER ~ YOU GAY  ")
                                print()
                                retry()
                            else:
                                exit()
                            
                        else:
                            exit()
                    elif answer == 'n':
                        clearScreen()
                        print("Dia mati konyol untuk kedua kalinya karena kebodohannya menggunakan skill kuli Jawanya.")
                        input()
                        clearScreen()

                        console.print("[b bright_white on red1]  GAME OVER ~ LMAO  ")
                        print()
                        retry()
                    else:
                        exit()
                elif answer == 'n':
                    clearScreen()
                    print("Dia dilarang masuk ke kota oleh penjaga dan ia juga dilucuti semua barang bawaannya, karena ia terlihat seperti orang pengangguran yang ingin mencuri.")
                    input()
                    print("Dia pun kembali lagi menjadi seorang pengangguran dan menjadi seorang gembel.")
                    input()
                    clearScreen()

                    console.print("[b bright_white on red1]  GAME OVER  ")
                    print()
                    retry()
                else:
                    exit()
            elif answer == 'n':
                clearScreen()
                print("“Maaf saja, kau terlalu miskin sebaiknya kau membeli barang murahan saja dan pergi dari sini, pengangguran sialan!” kata si penjual.")
                input()
                clearScreen()

                console.print("[b bright_white on red1]  GAME OVER ~ LOL NT  ")
                print()
                retry()
            else:
                exit()
            
        elif answer == 'n':
            clearScreen()
            print("Sayang sekali pada saat itu kamar kecil di minimarket sedang direnovasi, ia pun terpaksa membuang di celananya sendiri.")
            input()
            clearScreen()

            console.print("[b bright_white on red1]  GAME OVER  ")
            print()
            retry()
        else:
            exit()

# Main Menu
    clearScreen()
    table = Table(title = "WELCOME TO TEXT-BASED ADVENTURE")
    table.add_column("No", style = "cyan")
    table.add_column("Judul", style = "magenta")
    table.add_column("Genre", style = "sea_green3")
    table.add_row("1", "Man vs. The Forest", "Survival/Mystery")
    table.add_row("2", "Unemployed Reincarnated", "Fantasy/Isekai")
    console.print(table)

    print()
    console.print("[b sky_blue2]<I>[/] [sky_blue2]Pilih sebuah cerita untuk mulai!")
    story = console.input("[b sea_green3]<A>[/] ")
    print()

    if story == '1':
        clearScreen()
        print(title1)
        hint()
        clearScreen()
        story1()

    elif story == '2':
        clearScreen()
        print(title2)
        hint()
        clearScreen()
        story2()
        
    else:
        console.print("[b sky_blue2]<I>[/] [sky_blue2]Input tidak valid!")
        print()
        exit()

main()