
import streamlit as st
import webbrowser
import requests
background_color = """
    <style>
    body {
        background-color: #ffffff; 
    }
    </style>
"""
st.markdown(background_color, unsafe_allow_html=True)

#audio_url = "https://dl2.sura.pw/dl/reciter/1/32/001.mp3?h=tpbF6zaHPnBUmdu54vcwoQ&expires=1695739962&dl=true"
image_url = "https://j.top4top.io/p_2824pxkzj1.jpg"
audio_url='https://ia801400.us.archive.org/34/items/duaa-ommy_001/002.mp3'
st.markdown("""
    <div style='text-align:center; font-size: 40px;'>
        المرحوم قويدر العلاونه
    </div>
""", unsafe_allow_html=True)
# Button to show box
if st.button("دعاء للمرحوم"):
    st.markdown("""
    <div style='border: solid 2px black; padding: 10px; margin-top: 20px;'>
<p style='font-size: 20px; text-align: right;'> اللهم أسكنه فسيح الجنان واغفر له يا رحمن وارحم يا رحيم وتجاوز عما تعلم يا عليم.  </p>
<p style='font-size: 20px; text-align: right;'>  اللهم إن رحمتك وسعت كل شيء فارحمه رحمة تطمئن بها نفسه وتقر به عينه. </p>
<p style='font-size: 20px; text-align: right;'> اللهم احشره مع المتقين إلي الرحمن وفدًا. اللهم احشره مع أصحاب اليمين واجعل تحيته سلام لك من أصحاب اليمين.  </p>
<p style='font-size: 20px; text-align: right;'> اللهم اجعله من الذين سعدوا في الجنة خالدين فيها ما دامت السماوات والأرض.  </p>
<p style='font-size: 20px; text-align: right;'>اللهمّ املأ قبره بالرّضا، والنّور، والفسحة، والسّرور.   </p>
<p style='font-size: 20px; text-align: right;'> اللهمّ إنّا نتوسّل بك إليك، ونقسم بك عليك أن ترحمه ولا تعذّبه، وأن تثبّته عند السّؤال.  </p>
<p style='font-size: 20px; text-align: right;'>  اللهمّ إنّه في ذمّتك وحبل جوارك، فقِهِ فتنة القبر، وعذاب النّار، وأنت أهل الوفاء والحقّ، فاغفر له وارحمه، إنّك أنت الغفور الرّحيم. </p>
<p style='font-size: 20px; text-align: right;'> اللهم إنه كان مصلي لك، فثبنه على الصراط يوم تزل الأقدام. اللهم إنه كان صائم لك، فأدخله الجنة من باب الريان.  </p>
<p style='font-size: 20px; text-align: right;'> اللهم اغفر لحينا وميتنا وشاهدنا وغائبنا وصغيرنا وكبيرنا وذَكّرنَا وأنثانا.  </p>
<p style='font-size: 20px; text-align: right;'>  اللهم لا تحرمنا أجره ولا تضللنا بعده. </p>
    </div>
    """, unsafe_allow_html=True)
    
#apk_url = 'https://l.top4top.io/f_eN6KKkqUn9UVGKhFATow-g/1695914236/2825t11sv1.apk'

#file_url ='https://apk.e-droid.net/apk/app2846252-1wyg76.apk?v=1'

if st.button("لتحميل التطبيق"):
    apk_url = 'https://apk.e-droid.net/apk/app2846252-1wyg76.apk?v=1'
    st.markdown(f'<a href="{apk_url}" target="_blank">انقر هنا</a>', unsafe_allow_html=True)

audio_html = f"""
    <audio autoplay controls style="display: none">
        <source src="{audio_url}" type="audio/mp3">
        Your browser does not supoprt the audio element.
    </audio>
"""
# Image URL
image_url = "https://j.top4top.io/p_2824pxkzj1.jpg"
# Image HTML
image_html = f"""
    <style>
        @media only screen and (max-width: 600px) {{
            img {{
                width: 100%;
            }}
        }}
        @media only screen and (min-width: 600px) {{
            img {{
                width: 50%;
            }}
        }}
    </style>
    <img src="{image_url}">
"""
st.markdown(audio_html, unsafe_allow_html=True)
st.markdown(image_html, unsafe_allow_html=True)

