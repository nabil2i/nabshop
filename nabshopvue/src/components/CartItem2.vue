<template>
<div>
  <div class="card rounded-3 mb-4">
    <div class="card-body p-4">
      <div class="row d-flex justify-content-between align-items-center">
      <router-link :to="item.bookedition.get_id_url">
        <div class="col-md-2 col-lg-2 col-xl-2">
          <img
            src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-shopping-carts/img1.webp"
            class="img-fluid rounded-3" alt="Cotton T-shirt">
        </div>
        <div class="col-md-3 col-lg-3 col-xl-3">
          <p class="lead fw-normal mb-2">{{ item.bookedition?.book?.title }}</p>
          <!-- <p><span class="text-muted">Size: </span>M <span class="text-muted">Color: </span>Grey</p> -->
          <p><span class="text-muted">Unit price:</span> {{ item.bookedition.unit_price }} </p>
        </div>
      </router-link>
        <div class="col-md-3 col-lg-3 col-xl-2 d-flex">
          <button class="btn btn-link px-2"
            onclick="this.parentNode.querySelector('input[type=number]').stepDown()">
            <i class="fas fa-minus"></i>
          </button>

          <input id="form1" min="0" name="quantity" type="number"
            class="form-control form-control-sm"
            v-model="item.quantity"/>

          <button class="btn btn-link px-2"
            onclick="this.parentNode.querySelector('input[type=number]').stepUp()">
            <i class="fas fa-plus"></i>
          </button>
        </div>
        <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
          <!-- <h5 class="mb-0">{{ item.total_price}}</h5> -->
          <h5 class="mb-0">{{ getItemTotal(item).toFixed(2) }}</h5>
        </div>
        <div class="col-md-1 col-lg-1 col-xl-1 text-end">
          <a href="#!" class="text-danger"><i class="fas fa-trash fa-lg"></i></a>
        </div>
      </div>
    </div>
  </div>

</div>
  
</template>

<script>

export default {
  name: 'CartItem',
  props: {
    initialItem: Object
  },
  components: {

  },
  data() {
    return {
      item: this.initialItem
    };
  },
  mounted() {
   
  },
  computed: {

  },
  methods: {
    getItemTotal(item) {
      console.log(this.item)
      return item.quantity * item.bookedition.unit_price
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
