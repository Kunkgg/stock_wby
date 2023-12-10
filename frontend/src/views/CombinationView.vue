<template>
   <el-row justify="center">
        <el-col :span="6" class="grid-content">
            <el-statistic title="组合数量" :value="combinationCount" style="padding-top: 2rem;"/>
            <el-button type="primary" @click="dialogVisible = true" size="small">创建组合</el-button>
        </el-col>
    </el-row>

    <el-row :gutter="20" style="margin-top: 2rem;" justify="center">
        <el-col :sm="16" :md="8" :lg="6" v-for="index in 12" :key="`card-${index}`" class="grid-content">
            <combination-card @click="handleClickCard"></combination-card>
        </el-col>
    </el-row>
  <el-dialog
    v-model="dialogVisible"
    title="创建组合"
    width="60%"
  >
    <combination-create ref="child" :key="`creator-${creatorIndex}`"></combination-create>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleCreateCancel">取消</el-button>
        <el-button type="primary" @click="handleCreateConfirm">确认</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import CombinationCreate from "@/components/CombinationCreate.vue";
import CombinationCard from "@/components/CombinationCard.vue";

const combinationCount= ref(0);

const child = ref(null);
const dialogVisible = ref(false);

const router = useRouter();

const handleCreateConfirm = () => {
  dialogVisible.value = false;
  console.log("confirm");
  console.log(child.value.combinationName);
  console.log(child.value.combinationDescription);
  console.log(child.value.settingStocks);
};

let creatorIndex = ref(0);
const handleCreateCancel = () => {
  dialogVisible.value = false;
  creatorIndex.value++;
  console.log("cancel");
};

const handleClickCard = () => {
  console.log("click card");
  // 使用 router 跳转到 CombinationDetailView
  router.push({ name: "combination-detail", params: {combinationId: 1} });
};

</script>

<style scoped>
.grid-content {
  border-radius: 4px;
  min-height: 2rem;
  text-align: center;
  margin: 10px 0;
}
</style>


