import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useProductStore = defineStore("product", () => {
  let id = 1;
  const products = ref([
    { id: id++, title: "Product 1", body: "내용" },
    { id: id++, title: "Product 2", body: "내용내용" },
    { id: id++, title: "Product 3", body: "내용내용내용" },
  ]);
  return { products };
});
