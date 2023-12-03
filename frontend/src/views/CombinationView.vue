<template>
  <el-empty>
    <el-button type="primary" @click="dialogVisible = true">创建组合</el-button>
  </el-empty>

  <el-dialog
    v-model="dialogVisible"
    title="创建组合"
    width="60%"
  >
    <combination-create></combination-create>
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

const dialogVisible = ref(false);

const handleCreateConfirm = () => {
  dialogVisible.value = false;
  console.log("confirm");
};
const handleCreateCancel = () => {
  dialogVisible.value = false;
  console.log("cancel");
};

</script>



