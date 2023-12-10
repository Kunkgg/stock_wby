<template>
    <el-card shadow="hover" class="box-card">
        <span>{{ combinationName }}</span>
    </el-card>
</template>
<script setup>
import { ref, computed } from 'vue'
import { Edit } from '@element-plus/icons-vue'
import { Delete } from '@element-plus/icons-vue'

const combinationName = ref('组合名称')
const combinationDescription = ref('组合描述')
const stockCount = ref(0)
const updateCount = ref(0)
const updateTime = ref('xxxx-xx-xx xx:xx:xx')

</script>
<style scoped>
.box-card {
    min-height: 6rem;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>