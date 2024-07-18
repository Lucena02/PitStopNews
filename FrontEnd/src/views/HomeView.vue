<script setup lang="ts">
import { ref, onMounted } from 'vue';
import singleNews from './../components/singleNews.vue';

const newsData = ref<any[]>([]);

onMounted(async () => {
  try {
    const response = await fetch('https://newsapi.org/v2/top-headlines?q=Politics&from=2024-07-14&sortBy=popularity&apiKey=1e0cb31343434c79ad15803dbfd5e1dd');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    newsData.value = data.articles;
    console.log(newsData);
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
});
</script>

<template>
  <main>
    <div class="container">
      <div class="grelha">
        <singleNews 
          v-if="newsData[0]"
          :news="newsData[0]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="newsData[1]"
          :news="newsData[1]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="newsData[2]"
          :news="newsData[2]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="newsData[3]"
          :news="newsData[3]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="newsData[4]"
          :news="newsData[4]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="newsData[5]"
          :news="newsData[5]" 
          class="grelha-item"
        />
      </div>
    </div>
  </main>
</template>

<style>
* {
    margin: 0;
  }

.container{
  display:flex;
  justify-content: center;
  align-items: center;
  margin-top: 50px;
}

.grelha{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
}

@media  (max-width: 800px) {
    .grelha{
      display: block;
      margin-top: 10px;
    }
    .grelha-item {
      margin-bottom: 10px; /* Adjust this value to set the gap between items */
    }
}

</style>
