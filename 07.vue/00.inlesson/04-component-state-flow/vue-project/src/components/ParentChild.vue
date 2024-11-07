<template>
  <div>
    <!-- <h2>ParentChild</h2> -->
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild :my-msg="myMsg" @update-name="updateName" />

    <!-- <button @click="$emit('someEvent')">클릭!</button> -->
    <button @click="buttonClick">클릭!</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
// 내려받은 props 선언
// 방식이 달라도 출력은 똑같음! but, 객체 선언 방식을 더 권장!
// 1. 배열 선언 방식
// 선언할 때와 네이밍케이스가 달라 주의! (HTML vs JS)
// defineProps(["myMsg"]);

// 2. 객체 선언 방식
defineProps({
  myMsg: String,
  dynamicProps: String,
});

// props 데이터를 활용해야하는 경우
// console.log(props);
// console.log(props.myMsg);

import ParentGrandChild from "@/components/ParentGrandChild.vue";

// emit 이벤트 선언 (배열방식, 객체방식)
const emit = defineEmits(["someEvent, emitArgs"]);
const buttonClick = function () {
  emit("someEvent");
};
const emitArgs = function () {
  emit("emitArgs", 1, 2, 3);
};

const updateName = function () {
  emit("updateName");
};
</script>

<style scoped></style>
