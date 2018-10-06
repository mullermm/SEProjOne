package testing;

/**
 * @author Joseph Miller
 */

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import scanner.Course;

class joetest {

	@BeforeEach
	void setUp() throws Exception {

	}

	@AfterEach
	void tearDown() throws Exception {
	}

	@Test
	void test() {

		Course test = new Course("Intro to something", 4.2, "this course is blaj", 320, "com sci", "other classes");
		System.out.println(test);

	}

}
