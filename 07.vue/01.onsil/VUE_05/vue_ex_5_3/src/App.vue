<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList :products="products" @add-to-cart="addToCart" />
    <hr />
    <p>총 가격: {{ totalPrice }}원</p>
    <Cart :cart="cart" @delete-item="deleteItem" />
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import ProductList from "@/components/ProductList.vue";
import Cart from "@/components/Cart.vue";

let id = 0;

const products = ref([
  { id: id++, name: "사과", price: 1000 },
  { id: id++, name: "바나나", price: 1500 },
  { id: id++, name: "딸기", price: 2000 },
  { id: id++, name: "포도", price: 3000 },
  { id: id++, name: "복숭아", price: 2000 },
  { id: id++, name: "수박", price: 5000 },
]);
const cart = ref([]);

const addToCart = function (product) {
  const existingItem = cart.value.find((item) => item.id === product.id);
  if (existingItem) {
    existingItem.quantity = (existingItem.quantity || 1) + 1;
  } else {
    cart.value.push({ ...product, quantity: 1 });
  }
  // console.log(cart.value);
};

const totalPrice = computed(() => {
  return cart.value.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );
});

const deleteItem = function (item) {
  const idx = cart.value.findIndex((c) => c.id === item.id);
  if (idx !== -1) {
    cart.value.splice(idx, 1);
  }
};
</script>
