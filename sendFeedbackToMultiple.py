import smtplib
import sys

studentids=["RCA0201NSZ", "RCA0202JIZ", "RCA0203NMZ", "RCA0204ZUR", "RCA0205HDV", "RCA0206AKB", "RCA0207RVY", "RCA0208ZAK", "RCA0209ZNK", "RCA0210GNU", "RCA0211ZXU", "RCA0212RKE", "RCA0213KKA", "RCA0214KTL", "RCA0215HDC", "RCA0216EBG", "RCA0217NVS", "RCA0218NKA", "RCA0219SJH", "RCA0220KYT", "RCA0221DMU", "RCA0222SIT", "RCA0223UTZ", "RCA0224AXZ", "RCA0225DYY", "RCA0226LDV", "RCA0227XIJ", "RCA0228MWW", "RCA0229WBR", "RCA0230BLW", "RCA0231RBI", "RCA0232LUJ", "RCA0233EAM", "RCA0234MGD", "RCA0235YGN", "RCA0236VGD", "RCA0237MBR", "RCA0238CWM", "RCA0239HRZ", "RCA0240TKU", "RCA0241RBM", "RCA0242YUV", "RCA0243HGY", "RCA0244DYI", "RCA0245PVK", "RCA0246HGK", "RCA0247BJW", "RCA0248GPB", "RCA0249PII", "RCA0250HTR", "RCA0251SKX", "RCA0252BUT", "RCA0253VCB", "RCA0254IRL", "RCA0255LYI", "RCA0256JIW", "RCA0257AIZ", "RCA0258DDA", "RCA0259TEE", "RCA0260EZE"]

studentnames=["Igirimpuhwe Aime", "Biziyaremye Henriette", "Burigo Aldo Jabes", "Bwiza Nina", "Byiringiro Saad", "Dabagire Valens", "Dufitumukiza Emmanuel", "Dukunde Irakoze Acele Happy", "Dushime Grace Fidele", "Dushime Bill Benon", "Dushimimana Sandrine", "Gashugi Muhimpundu Adeline", "Gikundiro Larissa Teta", "Girishya Fiat Bruno", "Igihozo Marie Colombe", "Ihozo Marie Honnette", "Imanzi Yannick Kenny", "Impano Alliance", "Ineza Naillah", "Ineza Ange Michaella", "Ineza Jost Chance", "Iradukunda Clarisse", "Iradukunda Verite", "Irategeka Neza Bruce", "Ishimwe Teta Lena", "Isite Yves", "Itetero Ariane", "Kalisa Belyse", "Kamala Fidele", "Karera Marvin", "Kayigire Ngabire Kethia", "Kayitare Audax", "Kunda Mugisha Sarah", "Mfitumukiza Peter", "Mizero Eloi", "Mpano Christian", "Mudahemuka Manzi", "Muhire Patrick", "Muhoza Olivier Ivan", "Munganyinka Shakira ga", "Mutegetsi Prince", "Mwizera Amen Gisele", "Niyigena Tresor", "Niyigena Yves", "Nkubito Pacis", "Nshuti Jabes", "Ntagungira Ali Rashid", "Rugero Beulla", "Rutayisire Ange Belard", "Rwagapfizi Igor Roggy", "SETH ABIJURU", "Shumbusho David", "Shumbusho Ishimwe Anglebert", "Singizwa Nick", "Teta Butera Nelly", "Turinumugisha Souvenir", "Umuhoza Esther", "Umutoniwabo Hasbiyallah", "Uwamungu Gasaro Marie Leila", "Uwenayo Alain Pacifique"]

studentemails=["igaimerca@gmail.com", "hopebiziyaremye@gmail.com", "burigoj2@gmail.com", "ninamyles2020@gmail.com", "byiringirosaad@gmail.com", "valensdabagire@gmail.com", "dufitumukizaemmanuel0@gmail.com", "acele4444@gmail.com", "gngrace10@gmail.com", "DushimeBillBenon@gmail.com", "sanrdushimimana@gmail.com", "aderlinecarmella@gmail.com", "tetalarissa69@gmail.com", "fiatbruno10@gmail.com", "igihozocolombe2003@gmail.com", "ihozohonnette12@gmail.com", "imanziyannickkenny@gmail.com", "alliekook03@gmail.com", "NAILLAINEZA@gmail.com", "michaellaineza13@gmail.com", "jinezachance@gmail.com", "ciradukundaa@gmail.com", "veriteiradukunda14@gmail.com", "nezabruce@gmail.com", "tetalenaa@gmail.com", "yvesisite@gmail.com", "arianeitetero@gmail.com", "kalisabelyseteta@gmail.com", "kamalafizzet45@gmail.com", "kareramarvin14@gmail.com", "kemykayigire@gmail.com", "kayitareauda@gmail.com", "mugishakundasarah@gmail.com", "mfitep6@gmail.com", "eloimizero123@gmail.com", "mpanoc6@gmail.com", "mmanzicder@gmail.com", "pmuhire2002@gmail.com", "moikalasa12@gmail.com", "munganyinkashakira@gmail.com", "mutegetsi2000@gmail.com", "mamengisele@gmail.com", "niyigenatreasure@gmail.com", "wizynives@gmail.com", "pacisnkubito@gmail.com", "nshutij7@gmail.com", "ntagungiraali@gmail.com", "beullarugero7@gmail.com", "angebelard@gmail.com", "rwagapfizi10@gmail.com", "abiheloaf@gmail.com", "davidshumbusho10@gmail.com", "anglebertsh@gmail.com", "singizwanick19@gmail.com", "buteranelly250@gmail.com", "turinumugishasouvenir@gmail.com", "eumuhoza83@gmail.com", "umutoniwabohasby@gmail.com", "gasaroleila2018@gmail.com", "uwenayoallain@gmail.com"]

studentmarks=["10", "10", "10", "10", "9", "10", "8.5", "9", "9", "9", "10", "10", "10", "9", "9", "9", "10", "10", "9", "10", "10", "10", "9", "10", "10", "10", "10", "10", "10", "10", "10", "9", "9", "9", "10", "9", "10", "10", "10", "9", "9", "9", "10", "9", "9", "8.5", "10", "10", "10", "9", "10", "10", "9", "10", "9", "9.5", "8", "9", "10", "9"]

studentfeedback=["Great work!", "Great work!", "Great work!", "Great work!", "Your history.txt file could not be found.", "Great work!", "Your history.txt file could not be found. This IP 192.243.61.202 looks mistyped.", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Great work!", "Great work!", "Great work!", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Great work!", "Great work!", "Your history.txt file could not be found.", "Great work!", "Great work!", "Great work!", "Your history.txt file could not be found.", "Great work!", "Great work!", "Great work!", "Great work!", "Great work!", "Great work!", "Great work!", "Great work!", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Great work!", "Your history.txt file could not be found.", "Great work!", "Great work!", "Great work!", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Great work!", "Your history.txt file could not be found.", "Your history.txt file could not be found.", "Your history.txt file could not be found. This IP 192.243.61.202 looks mistyped.", "Great work!", "Great work!", "Great work!", "Your history.txt file could not be found.", "Great work!", "Great work!", "Your history.txt file could not be found.", "Great work!", "Your history.txt file could not be found.", "This IP 192.243.61.202 looks mistyped.", "Your history.txt file could not be found. You didn't show the public IP Address.", "Your history.txt file could not be found.", "Great work!", "Your history.txt file could not be found."]

course=["Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking", "Advanced Networking"]

date=["2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08", "2021-11-08"]

maximum=["10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10"]


for k in range(len(studentids)):
    print("\n")
    SUBJECT = "Feedback on CAT1 of "+course[k]   
    TEXT = "Dear "+studentnames[k]+",\n"
    TEXT += "I hope this email finds you well.\n\n"
    TEXT += "This is the feedback on CAT1 of "+course[k]+" done on "+date[k]+".\n"
    TEXT += "******************************\n"
    TEXT += "Score: "+studentmarks[k]+" out of "+maximum[k]+"\n"
    TEXT += "Feedback: "+studentfeedback[k]+"\n"
    TEXT += "******************************\n"
    TEXT += "\n"
    TEXT += "Best regards\n\n"
    TEXT += "Gabriel Baziramwabo\n"
    TEXT += "Instructor of Embedded Systems & Computer Networks\n"
    TEXT += "Rwanda Coding Academy (RCA)\n"

    msg = "Subject: {}\n\n{}".format(SUBJECT, TEXT)

    try:
        print("Sending email to "+studentnames[k]+"...\n")
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login ("gbaziramwabo@gmail.com", "B8AGYY@VPvxz6LRh")
        server.sendmail ("gbaziramwabo@gmail.com", studentemails[k], msg)
        server.quit()
    except:
        print("Email not sent to "+studentnames[k]+"\n")
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")