package com.radu.salesman.utils;

import com.itextpdf.text.*;
import com.itextpdf.text.pdf.PdfWriter;
import com.radu.salesman.domain.Order;
import com.radu.salesman.domain.OrderElement;
import com.radu.salesman.domain.User;

import java.io.FileOutputStream;

public class ExportPDF {
    private static String DEST = null;
    private static final Font titleFont = new Font(Font.FontFamily.TIMES_ROMAN, 24, Font.BOLD);
    private static final Font headerFont = new Font(Font.FontFamily.TIMES_ROMAN, 18, Font.BOLD);

    private final Order order;
    private final User user;
    private final float totalPrice;

    public ExportPDF(String destination, Order order, User user, float totalPrice) {
        DEST = destination;
        this.order = order;
        this.user = user;
        this.totalPrice = totalPrice;
    }

    public void write() {
        try {
            Document document = new Document();
            PdfWriter.getInstance(document, new FileOutputStream(DEST));
            document.open();
            addOrderDetails(document);
            addOrderContent(document);
            document.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void addOrderDetails(Document document) throws DocumentException {
        Paragraph orderDetails = new Paragraph();
        addEmptyLine(orderDetails, 1);
        Paragraph title = new Paragraph("Detaliile comenzii", titleFont);
        title.setAlignment(Element.ALIGN_CENTER);
        document.add(title);

        addEmptyLine(orderDetails, 3);
        orderDetails.add(new Paragraph("Adresa de livrare:", headerFont));
        orderDetails.add(new Paragraph(user.getPayment().getFullName()));
        orderDetails.add(new Paragraph("Jud. " + user.getContact().getCounty()));
        orderDetails.add(new Paragraph("Mun. " + user.getContact().getCity()));
        orderDetails.add(new Paragraph(user.getContact().getAddress()));
        addEmptyLine(orderDetails, 1);

        orderDetails.add(new Paragraph("Numarul comenzii:", headerFont));
        orderDetails.add(new Paragraph(String.valueOf(order.getId())));
        addEmptyLine(orderDetails, 1);

        orderDetails.add(new Paragraph("Modalitate de plata:", headerFont));
        orderDetails.add(new Paragraph("Card bancar"));
        addEmptyLine(orderDetails, 1);

        orderDetails.add(new Paragraph("Data comenzii:", headerFont));
        orderDetails.add(new Paragraph(Constants.DATE_TIME_FORMATTER.format(order.getDateTime())));
        addEmptyLine(orderDetails, 1);

        document.add(orderDetails);
    }

    private void addOrderContent(Document document) throws DocumentException {
        Paragraph orderContent = new Paragraph();
        addEmptyLine(orderContent, 2);
        Paragraph title = new Paragraph("Comanda", titleFont);
        title.setAlignment(Element.ALIGN_CENTER);
        document.add(title);

        addEmptyLine(orderContent, 1);
        for (OrderElement orderElement : order.getOrderElements()) {
            orderContent.add(new Paragraph(orderElement.getContent()));
        }
        addEmptyLine(orderContent, 1);
        orderContent.add(new Paragraph(String.format("Pret total:\t\t%.2f", totalPrice), headerFont));

        document.add(orderContent);
    }

    private static void addEmptyLine(Paragraph paragraph, int number) {
        for (int i = 0; i < number; i++) {
            paragraph.add(new Paragraph(" "));
        }
    }
}
