<template>

  <tr>
    <th scope="row">
      <div class="d-flex align-items-center">
        <img :src="item.bookedition.book.images[0].image"
          style="width: 120px;" alt="Book">
        <div class="flex-column ms-4">
          <p class="mb-2">{{ item?.bookedition?.book?.title }}</p>
          <p class="mb-0">{{ item?.bookedition?.book?.author }}</p>
        </div>
      </div>
    </th>
    <td class="align-middle">
      <p class="mb-0" style="font-weight: 500;">{{ item?.bookedition?.booktype}}</p>
    </td>
    <td class="align-middle">
      <p class="mb-0" style="font-weight: 500;"><span>$</span>{{ item?.bookedition?.unit_price}}</p>
    </td>
    <td class="align-middle">
      <div class="d-flex flex-row">
        <!-- <button class="btn btn-link px-2"
          onclick="this.parentNode.querySelector('input[type=number]').stepDown()"
          >
          <i class="fas fa-minus"></i>
        </button> -->
        <button class="btn btn-link px-2"
          @click="decrementQuantity(item)"
          >
          <i class="fas fa-minus"></i>
        </button>

        <input id="form1" min="0" name="quantity" v-model="item.quantity" type="number"
          class="form-control form-control-sm" style="width: 50px;" />

        <button class="btn btn-link px-2"
          @click="incrementQuantity(item)"
          >
          <i class="fas fa-plus"></i>
        </button>
        <!-- <button class="btn btn-link px-2"
          onclick="this.parentNode.querySelector('input[type=number]').stepUp()">
          <i class="fas fa-plus"></i>
        </button> -->
      </div>
    </td>
    <td class="align-middle">
      <p class="mb-0" style="font-weight: 500;"><span>$</span>{{ getItemTotal(item).toFixed(2) }}</p>
    </td>
    <td class="align-middle">
      <button class="" @click="removeFromCart(item)"><i class="fas fa-trash fa-lg"></i></button>  
    </td>
  </tr>

  
</template>

<script>

export default {
  name: 'CartItem2',
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
      // console.log(this.item)
      return item.quantity * item.bookedition.unit_price
    },
    incrementQuantity(item) {
      item.quantity += 1
      this.updateCart()
    },
    decrementQuantity(item) {
      item.quantity -= 1
      if (item.quantity === 0) {
       // this.$emit('removeFromCart', item)
      }
      this.updateCart()
    },
    updateCart() {
      // localStorage.setItem('cart', JSON.stringify(this.$store.cart))
    },
    removeFromCart(item) {
      // this.$emit('removeFromCart', item)

      this.updateCart()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
