import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useProductStore = defineStore("product", () => {
  const products = ref([
    { id: 1, title: "Product 1", body: "quia et suscipit suscipit recusandae" },
    { id: 2, title: "Product 2", body: "quo iure voluptatem occaecati omnis" },
    { id: 3, title: "Product 3", body: "repudiandae veniam quaerat sunt" },
  ]);

  const productCount = computed(() => products.value.length);

  const deleteProduct = function (productId) {
    // 요소를 직접 수정하는 대신에 splice 메서드를 사용하여 새로운 배열을 생성하여 상태를 업데이트
    const index = products.value.findIndex(
      (product) => product.id === productId
    );
    if (index !== -1) {
      products.value.splice(index, 1);
    }
  };

  const fetchProducts = () => {
    axios({
      method: "get",
      url: "https://jsonplaceholder.typicode.com/posts",
    })
      .then(function (res) {
        products.value = res.data;
        console.log("Products fetched successfully.");
      })
      .catch(function (err) {
        console.log("err");
      });
  };

  return { products, productCount, deleteProduct, fetchProducts };
});
