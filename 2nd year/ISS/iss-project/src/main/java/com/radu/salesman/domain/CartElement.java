/*
 * This code has been generated by the Rebel: a code generator for modern Java.
 *
 * Drop us a line or two at feedback@archetypesoftware.com: we would love to hear from you!
 */
package com.radu.salesman.domain;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import javax.persistence.Entity;

// ----------- << imports@AAAAAAF4esP5RG3S3bs= >>
// ----------- >>

// ----------- << class.annotations@AAAAAAF4esP5RG3S3bs= >>
// ----------- >>

@Entity
@Table(name = "CartElements")
public class CartElement extends com.radu.salesman.domain.Entity<Long> {
    // ----------- << attribute.annotations@AAAAAAF4esUOpm+bXW8= >>
    // ----------- >>
    private int quantity;

    // ----------- << attribute.annotations@AAAAAAF4esS1ym88MfE= >>
    // ----------- >>
    private Product product;

    // ----------- << attribute.annotations@AAAAAAF4eseVrnKEIac= >>
    // ----------- >>
    private Cart cart;

    private float price;

    public CartElement(int quantity, Product product, Cart cart, float price) {
        this.quantity = quantity;
        this.product = product;
        this.price = price;
        this.cart = cart;
    }

    public CartElement() {

    }

    @Id
    @GeneratedValue(generator="increment")
    @GenericGenerator(name="increment", strategy = "increment")
    @Override
    public Long getId() {
        return super.getId();
    }

    @Override
    public void setId(Long id) {
        super.setId(id);
    }

    @Column(name = "quantity")
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @OneToOne
    @JoinColumn(name = "productId", referencedColumnName = "id")
    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

    @ManyToOne
    @JoinColumn(name = "cartId", nullable = false)
    public Cart getCart() {
        return cart;
    }

    public void setCart(Cart cart) {
        this.cart = cart;
    }

    @Column(name = "price")
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "CartElement{" +
                ", quantity=" + quantity +
                ", product=" + product +
                '}';
    }
}
