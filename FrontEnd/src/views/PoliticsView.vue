<script setup lang="ts">
import { ref, onMounted } from 'vue';
import singleNews from './../components/singleNews.vue';

// Define reactive references for your data
const titles = ref<string[]>([]);
const images = ref<string[]>([]);
const links = ref<string[]>([]);
const sources = ref<string[]>([]);

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/politics');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();

    // Assign the fetched data to the reactive references
    titles.value = data.titles;
    images.value = data.images;
    links.value = data.links;
    sources.value = data.sources;


  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
});
</script>

<template>
  <main>
    <div class="container">
      <p v-if="titles.length === 0" class="noNews">No news available at the moment.</p>
      <div class="grelha">
        
        <singleNews 
          v-if="titles[0]"
          :title="titles[0]" 
          :image="images[0]" 
          :link="links[0]" 
          :source="sources[0]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="titles[1]"
          :title="titles[1]" 
          :image="images[1]" 
          :link="links[1]" 
          :source="sources[1]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="titles[2]"
          :title="titles[2]" 
          :image="images[2]" 
          :link="links[2]" 
          :source="sources[2]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="titles[3]"
          :title="titles[3]" 
          :image="images[3]" 
          :link="links[3]" 
          :source="sources[3]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="titles[4]"
          :title="titles[4]" 
          :image="images[4]" 
          :link="links[4]" 
          :source="sources[4]" 
          class="grelha-item"
        />
        <singleNews 
          v-if="titles[5]"
          :title="titles[5]" 
          :image="images[5]" 
          :link="links[5]" 
          :source="sources[5]" 
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


.noNews{
  margin-top: 5%;
  display:flex;
  color: var(--fontColor);
  font-family: Arial;
  font-weight: 600;
  font-size:3.4vw;
  align-items: center;
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
      margin-bottom: 15px;
    }
}

</style>
