<template>
  <h4>Timeline</h4>
  <el-timeline>
    <el-timeline-item
      v-for="(record, index) in records"
      :key="`record-${index}`"
      :record="record"
      :timestamp="record.update_time"
      placement="top"
    >
        <CombinationRecordCard></CombinationRecordCard>
    </el-timeline-item>
  </el-timeline>
</template>
<script setup>
import CombinationRecordCard from "./CombinationRecordCard.vue";
import { ref } from "vue";

const records = ref([
  {
    update_time: "2021-08-01 00:00:00",
  },
  {
    update_time: "2021-08-02 00:00:00",
  },
  {
    update_time: "2021-08-03 00:00:00",
  },
  {
    update_time: "2021-08-03 00:00:00",
  },
]);
</script>
