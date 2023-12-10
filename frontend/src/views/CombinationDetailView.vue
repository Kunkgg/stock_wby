<template>
    <el-page-header :icon="ArrowLeft" @back="handleBack" class="page-header">
    </el-page-header>
    <CombinationDetail></CombinationDetail>
    <CombinationTimeline></CombinationTimeline>
</template>
<script setup>
import { useRouter, useRoute } from 'vue-router';
import { ArrowLeft } from '@element-plus/icons-vue';
import { ref, watch, onMounted } from 'vue';
import CombinationDetail from '../components/CombinationDetail.vue';
import CombinationTimeline from '../components/CombinationTimeline.vue';

// go back
const router = useRouter()
const handleBack = () => {
    router.go(-1);
}

// watch route
const route = useRoute()
const combinationId = ref(null)
watch(route, (newRoute) => {
    combinationId.value = newRoute.params.combinationId
})

onMounted(() => {
    combinationId.value = route.params.combinationId
})

</script>

<style scoped>
.page-header {
    padding: 1.5rem;
    margin: .5px;
}
</style>