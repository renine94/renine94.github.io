/**
  Spring 에서 Get 요청 데이터 받는 방법
  - @PathVariable
  - @RequestParam (DTO)
 */


/**
  URL 의 path_variable 를 받는 방법
  http://localhost:8080/api/v1/variable1/{String 값}
 */

// 방법 1 - path {변수} 와 매개변수 이름이 같을 때
@GetMapping(value = "/variable1/{variable}")
public String getVariable1(@PathVariable String variable) {
  return variable;
}


// 방법 2 - path {변수} 와 매개변수 이름이 다를 때
@GetMapping(value = "/variable1/{variable}")
public String getVariable1(@PathVariable("variable") String var) {
  return var;
}


/**
  URL 의 query_string 를 받는 방법
  http://localhost:8080/api/v1/member?name=jaegu&email=renine94.dev@gmail.com&organization=fitpet
 */
@GetMapping(value = "/request1")
public String getRequestParam1(
  @RequestParam String name,
  @RequestParam String email,
  @RequestParam String organization) {
    return name + " " + email + " " + organization;
  }


@GetMapping(value = "/request2")
public String getRequestParam2(@RequestParam Map(String, String> param) {
  StringBuilder sb = new StringBuilder();

  // python - dict.items() 비슷한 느낌
  param.entrySet().forEach(map -> {
    sb.append(map.getKey() + " : " + map.getValue() + "\n");
  })

  return sb.toString();
})


@GetMapping(value = "/request3")
public String getRequestParam3(MemberDTO memberDTO) {
  return memberDTO.toString()
}


