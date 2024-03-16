from ff import *
#from tkinter import *
import tkinter as tk
import tkinter.font
import time
import schedule

window=tk.Tk()
window.title("smartmirror")
window.geometry("1020x568")
window.resizable(False, False)
window.configure(bg='black')

font_n=tkinter.font.Font(family="맑은 고딕", size=17, slant="roman")
font_1=tkinter.font.Font(family="맑은 고딕", size=20, slant="roman")
font_1n=tkinter.font.Font(family="맑은 고딕", size=17,weight='bold', slant="roman")
font_1t=tkinter.font.Font(family="맑은 고딕", size=60, weight='bold', slant="roman")
font_2=tkinter.font.Font(family="맑은 고딕", size=20, weight='bold', slant="roman")
font_3=tkinter.font.Font(family="맑은 고딕", size=20, weight='bold', slant="roman")
font_4=tkinter.font.Font(family="맑은 고딕", size=20, weight='bold', slant="roman")
font_5=tkinter.font.Font(family="맑은 고딕", size=23, weight='bold', slant="roman")

img = 0
def gui_set():
    global img
    
    frame1=LabelFrame(window, relief="solid", bd=2, background='white')
    frame1.place(x=30, y=20, width=440, height=310)

    frame1=LabelFrame(window,text='날씨', relief="solid", bd=2, background='black',foreground="white", font=font_n)
    frame1.place(x=35, y=25, width=430, height=300)

    frame2=LabelFrame(window, relief="solid", bd=2, background='white')
    frame2.place(x=480, y=20, width=500, height=130)

    frame2=LabelFrame(window, text='코로나 신규 확진', relief="solid", bd=2, background='black',foreground="white",font=font_n)
    frame2.place(x=485, y=25, width=490, height=120)

    frame3=LabelFrame(window,relief="solid", bd=2, background='white')
    frame3.place(x=480, y=150, width=500, height=180)

    frame3=LabelFrame(window, text='시간별 온도/강수확률',relief="solid", bd=2, background='black',foreground="white",font=font_n)
    frame3.place(x=485, y=155, width=490, height=170)

    frame4=LabelFrame(window, relief="solid", bd=2, background='white')
    frame4.place(x=30, y=330, width=950, height=220)

    frame4=LabelFrame(window,text='주간 날씨', relief="solid", bd=2, background='black',foreground="white",font=font_n)
    frame4.place(x=35, y=335, width=940, height=210)

    ####################오늘 날씨###############################
    dt = dt_wf()
    td_c= StringVar(); td_low = StringVar(); td_high = StringVar(); td_r = StringVar(); data_local = StringVar();
    td_pm10 = StringVar(); td_pm25 = StringVar(); td_n =dt[6] 
    td_c.set(dt[0]), td_low.set(dt[1]),  td_high.set(dt[2]), td_r.set(dt[3]+'%')
    td_pm10.set(dt[4]) , td_pm25.set(dt[5]), data_local.set(dt[7])

    l1=Label(window,textvariable=data_local , background='black',foreground="white",font=font_5)
    l1.place(x=60, y=70,)

    dt_hour = dt_hour_()
    dt_hour = int(dt_hour)

    image1 = 0
    if dt_hour <= 17 and dt_hour >= 6:
        if td_n == '맑음':
            img=tk.PhotoImage(file="낮.png")
        elif td_n == '구름조금':
            img=tk.PhotoImage(file="낮_구름.png")
        elif td_n == '구름많음':
            img=tk.PhotoImage(file="낮_구름.png")
        elif td_n == '흐림':
            img=tk.PhotoImage(file="흐림.png")
        elif td_n == '비':
            img=tk.PhotoImage(file="비.png")
        elif td_n == '눈':
            img=tk.PhotoImage(file="눈.png")
    else:
        if td_n == '맑음':
            img=tk.PhotoImage(file="밤.png")
        elif td_n == '구름조금':
            img=tk.PhotoImage(file="밤_구름.png")
        elif td_n == '구름많음':
            img=tk.PhotoImage(file="밤_구름.png")
        elif td_n == '흐림':
            img=tk.PhotoImage(file="흐림.png")
        elif td_n == '비':
            img=tk.PhotoImage(file="비.png")
        elif td_n == '눈':
            img=tk.PhotoImage(file="눈.png")
            
    l2=Label(window, image=img, background='black')
    l2.place(x=100, y=110)

    l3=Label(window, textvariable=td_c, background='black',foreground="white", font=font_1t)#온도
    l3.place(x=290, y=90)

    l4=Label(window, text='최고기온 ',background='black',foreground="white",font=font_n)
    l4.place(x=80, y=220)

    lg=Label(window, text=':',background='black',foreground="white",font=font_n)
    lg.place(x=178, y=217)

    ls=Label(window, textvariable=td_high, background='black',foreground="white",font=font_1n) #최고
    ls.place(x=190, y=220)

    l5=Label(window,text='최저기온 ',background='black',foreground="white",font=font_n)
    l5.place(x=260, y=220)

    lg=Label(window,text=':',background='black',foreground="white",font=font_n)
    lg.place(x=358, y=217)

    ld=Label(window, textvariable=td_low ,background='black',foreground="white",font=font_1n) #최저
    ld.place(x=370, y=220) 

    l6=Label(window,text='미세먼지 ',background='black',foreground="white",font=font_n)
    l6.place(x=60, y=270)

    lg=Label(window,text=':',background='black',foreground="white",font=font_n)
    lg.place(x=158, y=267)

    lf=Label(window, textvariable=td_pm10, background='black',foreground="white",font=font_1n) #미세
    lf.place(x=170, y=270)

    l7=Label(window,text='초미세먼지 ',background='black',foreground="white",font=font_n)
    l7.place(x=240, y=270)

    lg=Label(window,text=':',background='black',foreground="white",font=font_n)
    lg.place(x=358, y=267)

    lg=Label(window, textvariable=td_pm25, background='black',foreground="white",font=font_1n) #초미세
    lg.place(x=370, y=270)




    ####################코로나###############################
    ch = ch_()

    td_ch= StringVar(); td_local = StringVar()
    td_ch.set(ch[0]+'명'), td_local.set(ch[1]+'명')

    l50=Label(window, text='전국 ',background='black',foreground="white",font=font_2)
    l50.place(x=550, y=70)

    l51=Label(window, text=':',background='black',foreground="white",font=font_2)
    l51.place(x=610, y=67)

    l8=Label(window, textvariable=td_ch, background='black',foreground="white",font=font_2)#전국
    l8.place(x=620, y=70)

    l50=Label(window, text='대전 ',background='black',foreground="white",font=font_2)
    l50.place(x=760, y=70)

    l51=Label(window, text=':',background='black',foreground="white",font=font_2)
    l51.place(x=820, y=67)

    l11=Label(window,  textvariable=td_local, background='black',foreground="white",font=font_2)
    l11.place(x=830, y=70)

    ###################시간별 온도###########################
    srf = srf_()
    td_t1 =  StringVar(); td_c1 =  StringVar(); td_r1 =  StringVar()
    td_t2 =  StringVar(); td_c2 =  StringVar(); td_r2 =  StringVar()
    td_t3 =  StringVar(); td_c3 =  StringVar(); td_r3 =  StringVar()
    td_t4 =  StringVar(); td_c4 =  StringVar(); td_r4 =  StringVar()
    td_t1.set(srf[0][0]), td_c1.set(srf[1][0]), td_r1.set(srf[2][0])
    td_t2.set(srf[0][1]), td_c2.set(srf[1][1]), td_r2.set(srf[2][1])
    td_t3.set(srf[0][2]), td_c3.set(srf[1][2]), td_r3.set(srf[2][2])
    td_t4.set(srf[0][3]), td_c4.set(srf[1][3]), td_r4.set(srf[2][3])


    l12=Label(window, textvariable= td_t1, background='black',foreground="white",font=font_3) #시간1
    l12.place(x=530, y=200)

    l13=Label(window, textvariable= td_c1, background='black',foreground="white",font=font_3)
    l13.place(x=550, y=240)

    l13=Label(window, textvariable= td_r1, background='black',foreground="white",font=font_3)
    l13.place(x=540, y=280)


    l14=Label(window, textvariable= td_t2, background='black',foreground="white",font=font_3) #시간2
    l14.place(x=640, y=200)

    l15=Label(window, textvariable= td_c2, background='black',foreground="white",font=font_3)
    l15.place(x=660, y=240)

    l16=Label(window, textvariable= td_r2, background='black',foreground="white",font=font_3)
    l16.place(x=650, y=280)


    l17=Label(window,textvariable= td_t3, background='black',foreground="white",font=font_3) #시간3 
    l17.place(x=750, y=200)

    l18=Label(window, textvariable= td_c3, background='black',foreground="white",font=font_3)
    l18.place(x=770, y=240)

    l19=Label(window, textvariable= td_r3, background='black',foreground="white",font=font_3)
    l19.place(x=760, y=280)


    l20=Label(window, textvariable= td_t4, background='black',foreground="white",font=font_3) #시간4
    l20.place(x=860, y=200)

    l21=Label(window, textvariable= td_c4, background='black',foreground="white",font=font_3)
    l21.place(x=880, y=240)

    l22=Label(window, textvariable= td_r4, background='black',foreground="white",font=font_3)
    l22.place(x=870, y=280)

    ####################주간 날씨########################
    wk1 = wk1_()
    wk1_d =  StringVar(); wk1_r =  StringVar(); wk1_l =  StringVar(); wk1_h =  StringVar()
    wk1_d.set(wk1[0]), wk1_r.set(wk1[1]+'%'), wk1_l.set(wk1[2]), wk1_h.set(wk1[3])

    l29=Label(window, textvariable= wk1_d, background='black',foreground="white",font=font_4)
    l29.place(x=100, y=370)

    l30=Label(window, textvariable= wk1_r, background='black',foreground="white",font=font_4)
    l30.place(x=100, y=430)

    l31=Label(window, textvariable= wk1_l, background='black',foreground="white",font=font_4)
    l31.place(x=75, y=490)

    l32=Label(window,text='/',background='black',foreground="white",font=font_4)
    l32.place(x=115, y=490)

    l33=Label(window, textvariable= wk1_h, background='black',foreground="white",font=font_4)
    l33.place(x=133, y=490)

    ####################################################
    wk2 = wk2_()
    wk2_d =  StringVar(); wk2_r =  StringVar(); wk2_l =  StringVar(); wk2_h =  StringVar()
    wk2_d.set(wk2[0]), wk2_r.set(wk2[1]+'%'), wk2_l.set(wk2[2]), wk2_h.set(wk1[3])

    l29=Label(window, textvariable= wk2_d, background='black',foreground="white",font=font_4)
    l29.place(x=263, y=370)

    l30=Label(window, textvariable= wk2_r, background='black',foreground="white",font=font_4)
    l30.place(x=250, y=430)

    l31=Label(window, textvariable= wk2_l, background='black',foreground="white",font=font_4)
    l31.place(x=225, y=490)

    l32=Label(window,text='/',background='black',foreground="white",font=font_4)
    l32.place(x=263, y=490)

    l33=Label(window, textvariable= wk2_h, background='black',foreground="white",font=font_4)
    l33.place(x=283, y=490)
    ####################################################
    wk3 = wk3_()
    wk3_d =  StringVar(); wk3_r =  StringVar(); wk3_l =  StringVar(); wk3_h =  StringVar()
    wk3_d.set(wk3[0]), wk3_r.set(wk3[1]+'%'), wk3_l.set(wk3[2]), wk3_h.set(wk3[3])

    l29=Label(window, textvariable= wk3_d, background='black',foreground="white",font=font_4)
    l29.place(x=413, y=370)

    l30=Label(window, textvariable= wk3_r, background='black',foreground="white",font=font_4)
    l30.place(x=400, y=430)

    l31=Label(window, textvariable= wk3_l, background='black',foreground="white",font=font_4)
    l31.place(x=375, y=490)

    l32=Label(window,text='/',background='black',foreground="white",font=font_4)
    l32.place(x=413, y=490)

    l33=Label(window, textvariable= wk3_h, background='black',foreground="white",font=font_4)
    l33.place(x=433, y=490)

    ####################################################
    wk4 = wk4_()
    wk4_d =  StringVar(); wk4_r =  StringVar(); wk4_l =  StringVar(); wk4_h =  StringVar()
    wk4_d.set(wk4[0]), wk4_r.set(wk4[1]+'%'), wk4_l.set(wk4[2]), wk4_h.set(wk4[3])

    l29=Label(window, textvariable= wk4_d, background='black',foreground="white",font=font_4)
    l29.place(x=563, y=370)

    l30=Label(window, textvariable= wk4_r, background='black',foreground="white",font=font_4)
    l30.place(x=550, y=430)

    l31=Label(window, textvariable= wk4_l, background='black',foreground="white",font=font_4)
    l31.place(x=525, y=490)

    l32=Label(window,text='/',background='black',foreground="white",font=font_4)
    l32.place(x=563, y=490)

    l33=Label(window, textvariable= wk4_h, background='black',foreground="white",font=font_4)
    l33.place(x=583, y=490)

    ####################################################
    wk5 = wk5_()
    wk5_d =  StringVar(); wk5_r =  StringVar(); wk5_l =  StringVar(); wk5_h =  StringVar()
    wk5_d.set(wk5[0]), wk5_r.set(wk5[1]+'%'), wk5_l.set(wk5[2]), wk5_h.set(wk5[3])

    l29=Label(window, textvariable= wk5_d, background='black',foreground="white",font=font_4)
    l29.place(x=713, y=370)

    l30=Label(window, textvariable= wk5_r, background='black',foreground="white",font=font_4)
    l30.place(x=700, y=430)

    l31=Label(window, textvariable= wk5_l, background='black',foreground="white",font=font_4)
    l31.place(x=675, y=490)

    l32=Label(window,text='/',background='black',foreground="white",font=font_4)
    l32.place(x=713, y=490)

    l33=Label(window, textvariable= wk5_h, background='black',foreground="white",font=font_4)
    l33.place(x=733, y=490)

    ####################################################
    wk6 = wk6_()
    wk6_d =  StringVar(); wk6_r =  StringVar(); wk6_l =  StringVar(); wk6_h =  StringVar()
    wk6_d.set(wk6[0]), wk6_r.set(wk6[1]+'%'), wk6_l.set(wk6[2]), wk6_h.set(wk6[3])

    l29=Label(window, textvariable= wk6_d, background='black',foreground="white",font=font_4)
    l29.place(x=863, y=370)

    l30=Label(window, textvariable= wk6_r, background='black',foreground="white",font=font_4)
    l30.place(x=850, y=430)

    l31=Label(window, textvariable= wk6_l, background='black',foreground="white",font=font_4)
    l31.place(x=825, y=490)

    l32=Label(window,text='/',background='black',foreground="white",font=font_4)
    l32.place(x=863, y=490)

    l33=Label(window, textvariable= wk6_h, background='black',foreground="white",font=font_4)
    l33.place(x=883, y=490)

k =486
count = 0
count_r = 0
r = 0
while True:
    now = datetime.now()
    m = now.minute
    ad = srf_()
    ad_rt= ad[3]
    ad_rt= list(map(int, ad_rt))
    if m ==1 or k ==486:
        count += 1
        k =0
        gui_set()
        window.update()
        dtn = dt_wf()
        dtn = dtn[6]
        if count == 7:
            count = 0
            count_r = 0
        elif dtn =='비' or dtn =='눈':
            count_r = 1
            r = 1

        for i in range(6):
            if ad_rt[i] > 70:
                r = 1
                print(r)
        else:
            r = 0
            
        send_data=("A" + "," + str(r) + "," + str(count_r))
        client_socket.send(send_data)
        print(send_data)

        
        time.sleep(60)
    else:
        None
    time.sleep(1)




