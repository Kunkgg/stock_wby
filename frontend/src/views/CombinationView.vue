<template>
   <el-row justify="center">
        <el-col :span="6" class="grid-content">
            <el-statistic title="组合数量" :value="combinationCount" style="padding-top: 2rem;"/>
            <el-button type="primary" @click="dialogVisible = true" size="small">创建组合</el-button>
        </el-col>
    </el-row>

    <el-row>


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
import CombinationCreate from "@/components/CombinationCreate.vue";


const child = ref(null);

const dialogVisible = ref(false);

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

</script>

<style scoped>
.grid-content {
  border-radius: 4px;
  min-height: 2rem;
  text-align: center;
}
</style>


