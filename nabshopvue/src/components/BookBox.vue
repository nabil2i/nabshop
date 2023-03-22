<template>
<div>
  <div class="card">
            <img :src="book?.images?.[0]?.image" class="card-img-top" alt="">
            <div class="card-body">
              <div><h5 class="card-title"><strong>{{ book?.title }}</strong></h5></div>
              <div class="card-text">{{ book?.author }}</div>
              
              <div class=" row">
                <div class="col-lg-6 mt-3 d-flex justify-content-center">
                 
                  <!-- <a  class="btn btn-success btn-nabshop"><div>Buy paperback</div>$<span>{{ book.bookeditions?.[0]?.unit_price }}</span>
                  </a>  -->
                  <router-link :to="book.bookeditions?.[1]?.get_id_url" class=" btn btn-success btn-nabshop" aria-current="page">
                    <div>Paperback</div>$<span>{{ book.bookeditions?.[1]?.unit_price }}</span>
                  </router-link>
                </div>

                <div class="col-lg-6 mt-3 d-flex justify-content-center">
                  <!-- <a  class="btn btn-success btn-nabshop mb-2"><div>Buy Ebook</div>$<span>{{ book.bookeditions?.[2]?.unit_price }}</span>
                  </a> -->
                  <!-- <router-link to="/"  class=" btn btn-success btn-nabshop" aria-current="page">
                    <div>Buy Ebook</div>$<span>{{ book.bookeditions?.[2]?.unit_price }}</span>
                  </router-link> -->
                  <router-link :to="book.bookeditions?.[0]?.get_id_url" class=" btn btn-success btn-nabshop" aria-current="page">
                    <div>Ebook</div>$<span>{{ book.bookeditions?.[0]?.unit_price }}</span>
                  </router-link>
                </div>
              </div>
            </div>
          </div> 






  <!-- <div class="col"
     v-for="book in books"
     v-bind:key="book.id"
    >    
    <div class="card">
      <img :src="book.image[0].get_image" class="card-img-top" alt="">
      <div class="card-body">
        <div><h5 class="card-title"><strong>{{ book.title }}</strong></h5></div>
        <div class="card-text">{{ book.author }}</div>
        
        <div class="row mt-3">
          <div class="col-md-6 d-flex justify-content-center mb-2">
          
            <router-link href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy paperback</div>$<span>{{ book.bookeditions[0].unit_price }}</span>
            </router-link> 
          </div>

          <div class="col-md-6 d-flex justify-content-center">
      
            <a href="#" class="btn btn-success btn-nabshop mb-2" type="submit"><div>Buy Ebook</div>$<span>{{ book.bookeditions[1].unit_price }}</span></a> 
          </div>
        </div>
        View details
      </div>
    </div> 
  </div> -->
</div>
  
</template>

<script>

export default {
  name: 'BookBox',
  props: {
    book: Object
  },
  components: {

  },
  data() {
    return {
    };
  },
  mounted() {
 
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.btn-nabshop {
  width:120px;
}

.btn-nabshop:hover {
  background-color: rgb(99, 123, 154);
}
</style>
