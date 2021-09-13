import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import repository.ComputerRepairRequestRepository;
import repository.ComputerRepairedFormRepository;
import repository.file.ComputerRepairRequestFileRepository;
import repository.file.ComputerRepairedFormFileRepository;
import repository.jdbc.ComputerRepairRequestJdbcRepository;
import repository.jdbc.ComputerRepairedFormJdbcRepository;
import services.ComputerRepairServices;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

@Configuration
public class RepairShopConfig {
    @Bean
    static Properties getProps() {
        Properties properties = new Properties();
        try {
            System.out.println("Searching bd.config in directory" + (new File(".").getAbsolutePath()));
            properties.load(new FileReader("bd.config"));
        } catch (IOException ex) {
            System.err.println("Configuration file bd.config not found: " + ex);
        }
        return properties;
    }

    @Bean
    ComputerRepairRequestRepository requestsRepo() {
        return new ComputerRepairRequestJdbcRepository(getProps());
    }

    @Bean
    ComputerRepairedFormRepository formsRepo() {
        return new ComputerRepairedFormJdbcRepository(getProps());
    }

    @Bean
    @Primary
    ComputerRepairRequestRepository requestsRepo2() {
        return new ComputerRepairRequestFileRepository("ComputerRequests.txt");
    }

    @Bean
    @Primary
    ComputerRepairedFormRepository formsRepo2() {
        return new ComputerRepairedFormFileRepository("RepairedForms.txt", requestsRepo2());
    }

    @Bean
    ComputerRepairServices services() {
        return new ComputerRepairServices(requestsRepo2(), formsRepo2());
    }

}
