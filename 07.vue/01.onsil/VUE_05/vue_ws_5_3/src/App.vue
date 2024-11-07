<template>
  <div>
    <header>
      <h1>명함 관리 페이지</h1>
    </header>
    <main>
      <article>
        <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
      </article>
      <BusinessCard />
    </main>
    <footer>
      <p>ⓒ 2024 My Business Cards</p>
    </footer>
  </div>
</template>

<script setup>
import BusinessCard from "@/components/BusinessCard.vue";
</script>

<style scoped>
header {
  background-color: blue;
  color: white;
  text-align: center;
  padding: 50px;
  margin: 50px;
}
main {
  min-height: 500px;
  text-align: center;
}
article {
  text-align: center;
  min-height: 100px;
}
footer {
  text-align: center;
  background-color: gray;
  margin: 10px;
  padding: 10px;
}
</style>
