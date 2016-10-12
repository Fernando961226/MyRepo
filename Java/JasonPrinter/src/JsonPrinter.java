
import javax.json.*;


public class JsonPrinter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String json = Json.createObjectBuilder()
	            .add("key1", "value1")
	            .add("key2", "value2")
	            .build()
	            .toString();
		
		//System.out.println(json);
		
		
		
		JsonBuilderFactory factory = Json.createBuilderFactory(null);
		 JsonObject MetaResponse = factory.createObjectBuilder()
		     .add("Name", "checker-framework")
		     .add("DisplayName", "Checker Framework")
		     .add("Version","1.0")
		     .add("Email"," Ask Proffessor ------")
		     .add("SupportEmail"," Ask Proffessor ------")
		     .add("TermsOfUseUrl"," need website for the terms of use")
		     .add("PrivacyUrl"," need website for the privacy")
		     .add("Institution","University of Waterloo")
		     .add("InstitutionUrl","https://uwaterloo.ca/") // not sure if you want something more specific
		     .add("InstitutionImageUrl","https://uwaterloo.ca/brand-guidelines-and-tools/sites/ca.brand-guidelines-and-tools/files/resize/uploads/images/universityofwaterloo_logo_vert_rev_rgb_1-300x195.png")
		     .add("MimeType","???????")
		     .add("SupportsLanguageSyntax","flase") // check with proffessor 
		     .add("Title"," Checker Framework")
		     .add("Description"," A tool that allows for further checks in java language. Such as null pointer expections errors") //revise
		     .add("Question"," Could this program have any NullPointerException erros?") //revise
		     .add("Url","http://eisop.uwaterloo.ca/live#mode=display")
		     .add("VideoUrl"," (optional) gets the url to a page containing a video about the tool")
		     .add("DisableErrorTable"," false") //(optional) disables the parsing of the output to build the error table
		     .add("Samples", factory.createArrayBuilder()
		         .add(factory.createObjectBuilder()
		             .add("Name", "Nullness")
		             .add("Source", "????")) // check with professor
		         .add(factory.createObjectBuilder()
		             .add("Name", "MapKey")
		             .add("Source", "????"))) // check with professor
		     .add("Tutorials", factory.createArrayBuilder()
		    		 .add(factory.createObjectBuilder()
		    				 .add("Name", "Guide")
		    				 .add("Source", "# This is the markdown syntax test.\r\n\r\nA paragraph...\r\n\r\n    first\r\n\r\nThe tutorial also supports TeX maths through mathjax: \r\n\\[\\begin{aligned} \\dot{x} & = \\sigma(y-x) \\\\ \\dot{y} & = \\rho x - y - xz \\\\ \\dot{z} & = -\\beta z + xy \\end{aligned} \\]\r\n")
		    				 .add("Samples", factory.createArrayBuilder()
		    						 .add(factory.createObjectBuilder()
		    								 .add("Name", "Nullness")
		    					             .add("Source", "????")))))
		     .build();
		 
		 
		 JsonObject RunRequest = factory.createObjectBuilder()
			     .add("Version", "1.0")
			     .add("Source", "the source....")
				 .build();
		
		 
		 JsonObject RunResponce = factory.createObjectBuilder()
			     .add("Version", "1.0")
			     .add("Outputs", factory.createArrayBuilder()
				         .add(factory.createObjectBuilder()
				             .add("MimeType", "Nullness")
				             .add("Value", "# this is the text that you entered...")) // check with professor
				         .add(factory.createObjectBuilder()
				             .add("MimeType", "text/plain")
				             .add("Value", "This is the source...")))
				 .build();
		
		 JsonObject LanguageResponce = factory.createObjectBuilder()
			     .add("Version", "1.0")
			     .add("Version", "1.0")
			     .add("Version", "1.0")
			     .add("Version", "1.0")
			     .add("Outputs", factory.createArrayBuilder()
				         .add(factory.createObjectBuilder()
				             .add("MimeType", "Nullness")
				             .add("Value", "# this is the text that you entered...")) // check with professor
				         .add(factory.createObjectBuilder()
				             .add("MimeType", "text/plain")
				             .add("Value", "This is the source...")))
				 .build();
		
		 System.out.println(RunResponce.toString());
		 
		 
	}

}
