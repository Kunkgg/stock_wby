// import './assets/main.css'
import 'element-plus/dist/index.css'
import 'vxe-table/lib/style.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import ElTableInfiniteScroll from "el-table-infinite-scroll";
import VXETable from 'vxe-table'

function useTable (app) {
    app.use(VXETable)
}

const app = createApp(App)

app.use(router)
app.use(ElementPlus)
app.use(ElTableInfiniteScroll)
app.use(useTable)
app.mount('#app')
