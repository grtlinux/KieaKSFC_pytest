# Streamlit

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit](https://blog.zarathu.com/posts/2023-02-01-streamlit/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Privacy](https://streamlit.io/privacy-policy)
- [Streamlit API reference](https://docs.streamlit.io/library/api-reference)
- [treamlit cheat sheet](https://daniellewisdl-streamlit-cheat-sheet-app-ytm9sg.streamlit.app/)
- [Python Streamlit 사용법 - 프로토타입 만들기](https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/)
- []()
- []()
- []()
- []()
- []()
- []()


---
### pip install
``` shell
$ pip install streamlit
$ streamlit hello         <- demo page
```

### First
- app.py
``` python
# app.py

import streamlit as st

st.title('Hello streamlit')
```

- 실행
``` shell
$ streamlit run app.py
    👋 Welcome to Streamlit!

    If you’d like to receive helpful onboarding emails, news, offers, promotions,
    and the occasional swag, please enter your email address below. Otherwise,
    leave this field blank.

    Email:  grtlinux@gmail.com

    You can find our privacy policy at https://streamlit.io/privacy-policy

    Summary:
    - This open source library collects usage statistics.
    - We cannot see and do not store information contained inside Streamlit apps,
        such as text, charts, images, etc.
    - Telemetry data is stored in servers in the United States.
    - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
        creating that file if necessary:

        [browser]
        gatherUsageStats = false


    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://172.30.1.87:8501

    For better performance, install the Watchdog module:

    $ xcode-select --install
    $ pip install watchdog

```

- Browser check: http://localhost:8501  http://172.30.1.87:8501



