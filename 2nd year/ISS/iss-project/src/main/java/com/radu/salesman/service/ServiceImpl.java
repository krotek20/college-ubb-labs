/*
 * This code has been generated by the Rebel: a code generator for modern Java.
 *
 * Drop us a line or two at feedback@archetypesoftware.com: we would love to hear from you!
 */
package com.radu.salesman.service;

import com.radu.salesman.domain.*;
import com.radu.salesman.repository.*;
import com.radu.salesman.utils.Constants;
import com.radu.salesman.utils.ExportPDF;

import java.util.Collection;
import java.util.Date;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

// ----------- << imports@AAAAAAF4xoOmugG7rq0= >>
// ----------- >>

// ----------- << class.annotations@AAAAAAF4xoOmugG7rq0= >>
// ----------- >>

public class ServiceImpl implements Service {
    // ----------- << attribute.annotations@AAAAAAF5DxSpFVbIMs8= >>
    // ----------- >>
    private final UserRepository userRepository;

    // ----------- << attribute.annotations@AAAAAAF4fQSWZCf7klA= >>
    // ----------- >>
    private final ProductRepository productRepository;

    private final OrderRepository orderRepository;
    private final CartElementRepository cartElementRepository;
    private final OrderElementRepository orderElementRepository;

    public ServiceImpl(UserRepository userRepository, ProductRepository productRepository, OrderRepository orderRepository,
                       CartElementRepository cartElementRepository, OrderElementRepository orderElementRepository) {
        this.userRepository = userRepository;
        this.productRepository = productRepository;
        this.orderRepository = orderRepository;
        this.cartElementRepository = cartElementRepository;
        this.orderElementRepository = orderElementRepository;
    }

    // ----------- << method.annotations@AAAAAAF4xoQJewOuyC0= >>
    // ----------- >>
    @Override
    public User loginUser(User user) throws ServiceException {
        // ----------- << method.body@AAAAAAF4xoQJewOuyC0= >>
        // ----------- >>
        User currentUser = userRepository.findUser(user.getUsername(), user.getPassword());
        if (currentUser == null) {
            throw new ServiceException("Username or Password is incorrect!");
        }
        return currentUser;
    }

    // ----------- << method.annotations@AAAAAAF4xpcOgkm/6Rs= >>
    // ----------- >>
    @Override
    public Collection<Product> getProducts() {
        // ----------- << method.body@AAAAAAF4xpcOgkm/6Rs= >>
        // ----------- >>
        return StreamSupport
                .stream(productRepository.findAll().spliterator(), false)
                .collect(Collectors.toList());
    }

    @Override
    public CartElement addElementToCart(Product product, Cart cart, int quantity) {
        float price = product.getPrice() * quantity;
        return cartElementRepository.save(new CartElement(quantity, product, cart, price));
    }

    @Override
    public void removeCartElement(Long id) {
        cartElementRepository.delete(id);
    }

    @Override
    public Order generateOrder(User user, float totalPrice) {
        Order order = orderRepository.save(new Order(user, String.format("User %s has placed an order on %s",
                user.getPayment().getFullName(), Constants.DATE_TIME_FORMATTER.format(new Date()))));
        if (order != null) {
            user.getCart().getCartElements().forEach(x -> {
                OrderElement orderElement = orderElementRepository.save(
                        new OrderElement(order, String.format("%s\t\tx%d\t%.2f",
                                x.getProduct().getName(), x.getQuantity(), x.getPrice())));

                x.getProduct().setQuantity(x.getProduct().getQuantity() - x.getQuantity());
                modifyProduct(x.getProduct());
                cartElementRepository.delete(x.getId());
                order.addOrderElement(orderElement);
            });
            user.getCart().clearCartElements();
            ExportPDF exportPDF = new ExportPDF(String.format("src/main/resources/orders/Order%d.pdf", order.getId()),
                    order, user, totalPrice);
            exportPDF.write();
        }
        return order;
    }

    @Override
    public Product addProduct(Product product) {
        return productRepository.save(product);
    }

    @Override
    public void modifyProduct(Product product) {
        productRepository.update(product);
    }

    @Override
    public void deleteProduct(long productId) {
        productRepository.delete(productId);
    }
    // ----------- << class.extras@AAAAAAF4xoOmugG7rq0= >>
    // ----------- >>
}
