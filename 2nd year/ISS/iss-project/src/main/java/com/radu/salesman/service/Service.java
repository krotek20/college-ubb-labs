package com.radu.salesman.service;

import com.radu.salesman.domain.*;

import java.util.Collection;

public interface Service {
    User loginUser(User user) throws ServiceException;

    Collection<Product> getProducts();

    CartElement addElementToCart(Product product, Cart cart, int quantity);

    void removeCartElement(Long id);

    Order generateOrder(User user, float totalPrice);

    Product addProduct(Product product);

    void modifyProduct(Product product);

    void deleteProduct(long productId);
}
