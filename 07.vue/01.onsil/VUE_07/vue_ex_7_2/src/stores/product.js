import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useProductStore = defineStore("product", () => {
  const products = ref([
    { id: 1, title: "Product 1", body: "quia et suscipit suscipit recusandae" },
    { id: 2, title: "Product 2", body: "quo iure voluptatem occaecati omnis" },
    { id: 3, title: "Product 3", body: "repudiandae veniam quaerat sunt" },
  ]);
  const deleteTodo = function (selectedId) {
    const index = products.value.findIndex(
      (product) => product.id === selectedId
    );
    products.value.splice(index, 1);
  };
  const productCount = computed(() => {
    const product = products.value.length;
    return product;
  });
  return { products, deleteTodo, productCount };
});
