<template>
  <div class="parents-box">
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage
      v-for="child in family.children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
import ChildPage from "@/components/ChildPage.vue";
defineProps({
  family: Object,
});
</script>

<style scoped>
.parents-box {
  border: 1px solid black;
  background-color: rgb(241, 241, 241);
  text-align: center;
  margin: 10px;
}
</style>
