<template>
  <div>
    <!-- <h2>ColorChanger</h2> -->
    <input v-model="inputColor" type="text" />
    <p :style="{ color: inputColor }">
      입력창에 올바른 색상 명을 입력하면 글자색이 바뀌어요.
    </p>
  </div>
</template>

<script setup>
import { ref } from "vue";
const inputColor = ref("");
</script>

<style scoped>
.red {
  color: red;
}
.blue {
  color: blue;
}
.green {
  color: green;
}
</style>
