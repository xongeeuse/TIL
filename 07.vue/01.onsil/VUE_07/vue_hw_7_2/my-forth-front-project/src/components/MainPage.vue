<template>
  <div>
    <h1>Pinia 연! 습!</h1>
    <ParentPage
      v-for="family in store.familyInfo"
      :key="family.familyName"
      :family="family"
    />
  </div>
</template>

<script setup>
import ParentPage from "@/components/ParentPage.vue";
import { useFamilyStore } from "@/stores/family";
const store = useFamilyStore();
</script>

<style scoped></style>
