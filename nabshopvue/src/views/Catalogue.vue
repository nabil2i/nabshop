<template>
  <div class="home container catalogue">
    <h1>This is a catalogue page</h1>
    <Store/>
  </div> 
</template>

<script>
// @ is an alias to /src
import Store from '@/components/Store.vue'


export default {
  name: 'Catalogue',
  components: {
    Store
  }
}
</script>
