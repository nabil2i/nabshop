<template>

  <tr>
    <th scope="row">
      <div class="d-flex align-items-center">
        <img :src="item.bookedition.book.images[0].image"
          style="width: 120px;" alt="Book">
        <div class="flex-column ms-4">
          <p class="mb-2">{{ item.bookedition?.book?.title }}</p>
          <p class="mb-0">{{ item.bookedition?.book?.author }}</p>
        </div>
      </div>
    </th>

    <td class="align-middle">
      <p class="mb-0" style="font-weight: 500;">{{ item.bookedition?.booktype}}</p>
    </td>
    
    <td class="align-middle">
      <p class="mb-0" style="font-weight: 500;"><span>$</span>{{ item.quantity }}</p>
    </td>

    <td class="align-middle">
      <p class="mb-0" style="font-weight: 500;"><span>$</span>{{ getItemTotal(item).toFixed(2) }}</p>
    </td>
  </tr>

  
</template>

<script>

export default {
  name: 'CartItemCheckout',
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
    updateCart() {
      localStorage.setItem('cart', JSON.stringify(this.$store.cart))
    },
    removeFromCart(item) {
      this.$emit('removeFromCart', item)

      this.updateCart()
    }
  }
}
</script>

<style scoped lang="scss">

</style>
