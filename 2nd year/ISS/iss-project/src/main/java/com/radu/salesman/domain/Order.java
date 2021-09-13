/*
 * This code has been generated by the Rebel: a code generator for modern Java.
 *
 * Drop us a line or two at feedback@archetypesoftware.com: we would love to hear from you!
 */
package com.radu.salesman.domain;

import org.hibernate.annotations.GenericGenerator;
import org.hibernate.annotations.Type;
import org.hibernate.usertype.EnhancedUserType;

import java.time.Instant;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashSet;
import java.util.List;
import javax.persistence.*;
import javax.persistence.Entity;

// ----------- << imports@AAAAAAF4fPaHGBHdJB4= >>
// ----------- >>

// ----------- << class.annotations@AAAAAAF4fPaHGBHdJB4= >>
// ----------- >>

@Entity
@Table(name = "Orders")
public class Order extends com.radu.salesman.domain.Entity<Long> {
    // ----------- << attribute.annotations@AAAAAAF4fQBDvhx7PZ4= >>
    // ----------- >>
    private User user;

    // ----------- << attribute.annotations@AAAAAAF4fPmdhxR4tsY= >>
    // ----------- >>
    private Date date;

    // ----------- << attribute.annotations@AAAAAAF4fTiIaC63YB0= >>
    // ----------- >>
    private String comments;

    // ----------- << attribute.annotations@AAAAAAF4fQKS0CHxwbA= >>
    // ----------- >>
    private List<OrderElement> orderElements;

    public Order(User user, Date date, String comments, List<OrderElement> orderElements) {
        this.user = user;
        this.date = date;
        this.comments = comments;
        this.orderElements = orderElements;
    }

    public Order(User user, String comments) {
        this.user = user;
        this.date = new Date();
        this.comments = comments;
        this.orderElements = new ArrayList<>();
    }
    public Order() {

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

    @OneToOne
    @JoinColumn(name = "userId", referencedColumnName = "id")
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    @Temporal(TemporalType.TIMESTAMP)
    public Date getDateTime() {
        return date;
    }

    public void setDateTime(Date date) {
        this.date = date;
    }

    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    @OneToMany(mappedBy = "order", targetEntity = OrderElement.class, cascade = CascadeType.ALL)
    public List<OrderElement> getOrderElements() {
        return orderElements;
    }

    public void setOrderElements(List<OrderElement> orderElements) {
        this.orderElements = orderElements;
    }

    public void addOrderElement(OrderElement orderElement) {
        this.orderElements.add(orderElement);
    }

    @Override
    public String toString() {
        return "Order{" +
                ", user=" + user +
                ", dateTime=" + date +
                ", comments='" + comments + '\'' +
                '}';
    }
}
