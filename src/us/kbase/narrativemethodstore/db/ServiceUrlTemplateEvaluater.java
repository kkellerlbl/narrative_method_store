package us.kbase.narrativemethodstore.db;

import java.io.StringWriter;
import java.util.HashMap;
import java.util.Map;

import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;

import us.kbase.narrativemethodstore.exceptions.NarrativeMethodStoreException;

public class ServiceUrlTemplateEvaluater {
    private String endpointHost;
    private String endpointBase;
    private String endpoint = null;
    
    public ServiceUrlTemplateEvaluater(String endpointHost, String endpointBase) {
        this.endpointHost = endpointHost;
        this.endpointBase = endpointBase;
        if (endpointHost != null) {
            endpoint = endpointHost;
            if (endpointBase != null)
                endpoint += endpointBase;
        }
    }
    
    public String evaluate(String urlTemplate, String serviceVersion) 
            throws NarrativeMethodStoreException {
        try {
            StringWriter sw = new StringWriter();
            Map<String, String> context = new HashMap<String, String>();
            if (endpointBase != null)
                context.put("endpoint-base", endpointBase);
            if (endpointHost != null)
                context.put("endpoint-host", endpointHost);
            if (endpoint != null)
                context.put("endpoint", endpoint);
            if (serviceVersion != null)
                context.put("service-version", serviceVersion);
            VelocityContext cntx = new VelocityContext(context);
            Velocity.evaluate(cntx, sw, "ServiceUrlTemplate", urlTemplate);
            return sw.toString();
        } catch (Exception ex) {
            throw new NarrativeMethodStoreException("Problems with service url template " +
            		"evaluation: " + urlTemplate, ex);
        }
    }
}
