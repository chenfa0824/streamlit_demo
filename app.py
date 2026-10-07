# streamlit_app.py
import streamlit as st


# streamlit DEMO演示
demo0 = st.Page("streamlit/demo/demo0.py", title="demo0", icon="🏠")
demo1 = st.Page("streamlit/demo/demo1.py", title="demo1", icon="🏠")
demo2 = st.Page("streamlit/demo/demo2.py", title="demo2", icon="🏠")
demo3 = st.Page("streamlit/demo/demo3.py", title="demo3", icon="🏠")
demo4 = st.Page("streamlit/demo/demo4.py", title="demo4", icon="🏠")
sidebar1 = st.Page("streamlit/demo/sidebar1.py", title="sidebar1", icon="🏠")
sidebar2 = st.Page("streamlit/demo/sidebar2.py", title="sidebar2", icon="🏠")
tab1 = st.Page("streamlit/demo/tab1.py", title="tab1", icon="🏠")
tab2 = st.Page("streamlit/demo/tab2.py", title="tab2", icon="🏠")
table1 = st.Page("streamlit/demo/table1.py", title="table1", icon="🏠")
table2 = st.Page("streamlit/demo/table2.py", title="table2", icon="🏠")
# 动画
animation0 = st.Page("streamlit/demo/animation0.py", title="animation0", icon="🏠")
animation1 = st.Page("streamlit/demo/animation1.py", title="animation1", icon="🏠")
animation2 = st.Page("streamlit/demo/animation2.py", title="animation2", icon="🏠")
animation3 = st.Page("streamlit/demo/animation3.py", title="animation3", icon="🏠")
animation4 = st.Page("streamlit/demo/animation4.py", title="animation4", icon="🏠")
animation5 = st.Page("streamlit/demo/animation5.py", title="animation5", icon="🏠")
animation6 = st.Page("streamlit/demo/animation6.py", title="animation6", icon="🏠")

ui1 = st.Page("streamlit/ui/ui1.py", title="ui1", icon="📊")
ui2 = st.Page("streamlit/ui/ui2.py", title="ui2", icon="📊")
ui3 = st.Page("streamlit/ui/ui3.py", title="ui3", icon="📊")
elementui1 = st.Page("streamlit/ui/elementui1.py", title="elementui1", icon="🏠")
elementui2 = st.Page("streamlit/ui/elementui2.py", title="elementui2", icon="🏠")
elementui3 = st.Page("streamlit/ui/elementui3.py", title="elementui3", icon="🏠")



# 配置导航（可以分组）
pg = st.navigation({
    "Demo": [demo0, demo1, demo2, demo3, demo4, animation0, animation1, animation2, animation3, animation4,
             animation5, animation6, sidebar1, sidebar2, tab1, tab2, table1, table2
             ],
    # "UI": [ui1, ui2, ui3, elementui1, elementui2, elementui3
    # "Jacoco": [jacocoHtml, jacocoXml],
    # "工具": [xmind1, xmind2, crm_api, hrm_api, git_branch],
    # "项目": [liang1, liang2, liang3,mock1, mock2],

})

# 执行当前选中的页面
pg.run()
